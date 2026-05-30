# Save as log_counter.py
with open("failed_logins.txt", "r") as file:
    lines = file.readlines()

print(f"Total failed login attempts: {len(lines)}")

