import re
from getpass import getpass
from netmiko import ConnectHandler

# Example inventory: replace with all ABC routers and Layer 3 switches.
devices = {
    "SEA-R01": "192.168.16.1",
    "SEA-SW01": "192.168.16.2",
    "SEA-SW02": "192.168.16.3",
}

username = input("Username: ")
password = getpass("SSH password: ")
enable_secret = getpass("Enable secret, if required: ")

for name, address in devices.items():
    print(f"\n--- {name} ({address}) ---")

    try:
        with ConnectHandler(
            device_type="cisco_ios",
            host=address,
            username=username,
            password=password,
            secret=enable_secret,
            ssh_strict=True,
            system_host_keys=True,
            conn_timeout=10,
        ) as connection:
            if not connection.check_enable_mode():
                connection.enable()

            config = connection.send_command(
                "show running-config", read_timeout=30
            )

        if not config.strip() or re.search(r"^%.*", config, re.M):
            raise ValueError("Could not retrieve a valid configuration.")

        checks = {
            "SSH version 2": bool(
                re.search(r"^ip ssh version 2\s*$", config, re.M)
            )
        }

        vty_sections = list(re.finditer(
            r"^(line vty[^\n]*)\n((?:[ \t]+[^\n]*\n?)*)",
            config,
            re.M,
        ))

        checks["VTY configuration found"] = bool(vty_sections)

        for section in vty_sections:
            label, settings = section.groups()
            commands = {line.strip() for line in settings.splitlines()}
            checks[f"{label}: SSH only"] = (
                "transport input ssh" in commands
            )
            checks[f"{label}: local authentication"] = (
                "login local" in commands
            )

        for setting, passed in checks.items():
            status = "PASS" if passed else "REVIEW"
            print(f"{status}: {setting}")

    except Exception as error:
        print(f"ERROR: Device check incomplete: {error}")
