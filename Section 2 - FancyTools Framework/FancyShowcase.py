#!/usr/bin/env python3
# 🧪 FancyTools Showcase Demo Script
# Uses all available utilities from your fancytools module

from fancytools.fancy import (
    fancy_print,
    with_step_progress,
    create_panel,
    gradient_print,
    rich_table,
)

from rich.console import Console
from rich.layout import Layout

console = Console()

# 🌈 Demo 1: Gradient Welcome Message
def demo_gradient():
    gradient_print("🌈 Welcome to the FancyTools Showcase!", "#00BFFF", "#DA70D6")

# 🖨 Demo 2: Styled Fancy Prints
def demo_fancy_prints():
    fancy_print("🛠 Status: ", "Loading Tools...", random_color=True, random_style=True)
    fancy_print("🎯 Target: ", "Full Feature Demo", label_rainbow=True, rainbow=True)

# 📊 Demo 3: Step Progress Simulation
def demo_progress():
    tasks = [("🔍 Scanning Repos", 0.3), ("📦 Installing Modules", 0.4), ("✅ Complete", 0.2)]
    with_step_progress(tasks)

# 📋 Demo 4: Display Rich Table
def demo_table():
    headers = ["Tool", "Status", "Category"]
    rows = [
        ["fancy_print", "✅ Ready", "Styling"],
        ["gradient_print", "✅ Ready", "Text Effects"],
        ["with_step_progress", "✅ Ready", "Progress"],
        ["create_panel", "✅ Ready", "Layout"],
        ["rich_table", "✅ Ready", "Tables"],
    ]
    table = rich_table(headers, rows, title="📋 FancyTools Module Overview")
    console.print(table)

# 🪟 Demo 5: Panels with Nested Layouts
def demo_layout_panel():
    layout = Layout()
    layout.split_row(
        Layout(create_panel("💡 Left Side Info", title="Left Panel", border_style="green")),
        Layout(create_panel("📊 Right Side Data", title="Right Panel", border_style="cyan"))
    )
    console.print(layout)

# 🚀 Main
if __name__ == "__main__":
    console.rule("[bold magenta]🎉 FancyTools Demo Start 🎉")

    demo_gradient()
    console.rule("🔹 Fancy Prints 🔹")
    demo_fancy_prints()

    console.rule("🔹 Simulated Progress 🔹")
    demo_progress()

    console.rule("🔹 Table View 🔹")
    demo_table()

    console.rule("🔹 Panel Layout 🔹")
    demo_layout_panel()

    console.rule("[bold green]✅ FancyTools Demo Complete ✅")
