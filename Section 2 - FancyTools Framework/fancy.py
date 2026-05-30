# ~/python-playground/fancytools/fancy.py

from rich.console import Console
from rich.text import Text
from rich.color import Color
from rich.style import Style
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, TimeRemainingColumn, SpinnerColumn
from rich.syntax import Syntax
from rich.layout import Layout
import random
from time import sleep
from random import choice

console = Console()

# 🎨 Color dictionary
colors = {
    # 🎨 Basic named colors (Rich-native)
    "black": "black",
    "red": "red",
    "green": "green",
    "yellow": "yellow",
    "blue": "blue",
    "magenta": "magenta",
    "cyan": "cyan",
    "white": "white",
    
    # 💎 Bright variants
    "bright_red": "bright_red",
    "bright_green": "bright_green",
    "bright_yellow": "bright_yellow",
    "bright_blue": "bright_blue",
    "bright_magenta": "bright_magenta",
    "bright_cyan": "bright_cyan",
    "bright_white": "bright_white",
    
    "gold": "#ffd700",
    "silver": "#c0c0c0",
    "bronze": "#cd7f32",
    "hot_pink": "#ff69b4",
    "orchid": "#da70d6",
    "rust_orange": "#b7410e",
    "pastel_pink": "#ffc0cb",
    "mint_green": "#98ff98",
    "medium_purple": "#9370db",
    "sky_blue": "rgb(135,206,235)",
    "lavender": "rgb(181,126,220)",
    "lime": "#32cd32",
    "crimson": "#dc143c",
    "turquoise": "#40e0d0",
    "electric_blue": "#7df9ff",
    "sunset_orange": "#ff5e3a",
    "neon_green": "#39ff14",
    "royal_blue": "#4169e1",
    "peach": "#ffdab9",
    "slate_gray": "#708090",
    "canary_yellow": "#ffef00",
    "bubblegum_pink": "#ffb7c5",
    "aqua_marine": "#7fffd4",
    "charcoal": "#36454f",
    "tangerine": "#f28500",
    "deep_violet": "#9400d3",
    "sea_green": "#2e8b57",
    "coral": "#ff7f50",
    "fuchsia": "#ff00ff",
    "indigo": "#4b0082",
    "periwinkle": "#ccccff",
    "ice_blue": "#99ffff",
    
    # 🍬 New playful colors
    "plum": "#dda0dd",
    "rose": "#ff007f",
    "grape": "#6f2da8",
    "lemon": "#fff700",
    "pumpkin": "#ff7518",
    "forest_green": "#228b22",
    "midnight_blue": "#191970",
    "blush": "#de5d83",
    "sand": "#f4a460",
    "aqua": "#00ffff",
    "cyan": "#00ffff",
    "orchid": "#da70d6"
}

# 🖌 Style options
style_options = [
    "bold", "italic", "underline", "dim",
    "reverse", "bold italic", "bold underline"
]

# 🌈 Rainbow effect for text
def rainbow_text(text):
    rainbow = Text()
    color_vals = list(colors.values())
    for i, char in enumerate(str(text)):
        rainbow.append(char, style=color_vals[i % len(color_vals)])
    return rainbow

def fancy_print(
    label="",
    value=None,
    label_color="hot_pink",
    label_style="bold",
    value_color="mint_green",
    value_style="italic",
    label_rainbow=False,
    rainbow=False,
    random_style=False,
    random_color=False,
    style=None,         # ✅ New!
    color=None          # ✅ New!
):
    color_keys = list(colors.keys())

    # 🎨 Apply random styles/colors
    if random_color:
        label_color = random.choice(color_keys)
        value_color = random.choice(color_keys)

    if random_style:
        value_style = random.choice(style_options)

    # 🎯 Apply shortcut overrides if given
    if style:
        value_style = style
        label_style = style

    if color:
        value_color = color
        label_color = color

    label_hex = colors.get(label_color, "#ffffff")
    value_hex = colors.get(value_color, "#ffffff")

    # 🧱 Build Text() blocks
    label_text = (
        rainbow_text(str(label)) if label_rainbow
        else Text(str(label), style=f"{label_style} {label_hex}")
    )

    value_str = "" if value is None else str(value)
    value_text = (
        rainbow_text(value_str) if rainbow
        else Text(value_str, style=f"{value_style} {value_hex}")
    )

    console.print(label_text + value_text)
    return ""  # Prevent None from printing


def spaced_print(label, list_obj):
    """Prints a rainbow-styled label and a rainbow version of a list with space after."""
    console.print(rainbow_text(f"\n{label}"))
    console.print(rainbow_text(str(list_obj)))
    console.print("\n")

# 🚀 Animated Progress Bars
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, SpinnerColumn

def run_progress_demo():
    """Display a fake multi-step progress bar demo with beautiful animation."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold magenta]{task.description}"),
        BarColumn(bar_width=None),
        TextColumn("[cyan]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task1 = progress.add_task("[red]Processing data...", total=100)
        task2 = progress.add_task("[green]Analyzing results...", total=100)
        task3 = progress.add_task("[blue]Generating report...", total=100)

        for i in range(100):
            sleep(0.03)  # add a slight delay to make animation visible
            progress.update(task1, advance=1)
            progress.update(task2, advance=1)
            progress.update(task3, advance=1)

    console.print("\n[bold green]✅ All tasks completed! Tutorial complete.[/bold green]")

if __name__ == "__main__":
    run_progress_demo()

from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from time import sleep

def with_step_progress(description="Processing...", steps=10, delay=0.1, style="bold cyan"):
    """Display a live progress bar for a given number of steps."""
    with Progress(
        TextColumn("[progress.description]{task.description}", style=style),
        BarColumn(bar_width=None),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeRemainingColumn(),
    ) as progress:
        task = progress.add_task(f"{description}", total=steps)
        for _ in range(steps):
            sleep(delay)
            progress.update(task, advance=1)

def with_label_progress(steps, delay=0.2):
    """
    Animates a sequence of labeled steps using Rich progress bars.
    
    Args:
        steps (list): List of strings, each representing a step label.
        delay (float): Delay in seconds for each step (default: 0.2s).
    """
    with Progress(
        TextColumn("[bold magenta]{task.description}", justify="right"),
        BarColumn(),
        TextColumn("[cyan]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        transient=True,
    ) as progress:
        for step in steps:
            task = progress.add_task(f"{step}", total=100)
            for _ in range(100):
                sleep(delay)
                progress.update(task, advance=1)

def run_demo_progress():
    demo_steps = [
        "🔄 Initializing system...",
        "🔍 Loading data...",
        "🧠 Analyzing patterns...",
        "📊 Generating report...",
        "✅ Task completed!"
    ]
    with_label_progress(demo_steps, delay=0.02)

from rich.table import Table
from rich.console import Console

console = Console()

def rich_table(
    headers,
    rows,
    title="",
    header_style="bold cyan",
    row_style="dim",
    border_style="bright_magenta",
    show_lines=True,
    justify="center"
):
    """
    Print a dynamic Rich table with custom headers and rows.

    Args:
        headers (list): Column headers.
        rows (list of lists): Row data.
        title (str): Optional table title.
        header_style (str): Style for header row.
        row_style (str): Style for row content.
        border_style (str): Style for table border.
        show_lines (bool): Whether to show horizontal lines.
        justify (str): Alignment for all columns (left, center, right).
    """

    table = Table(
        title=title,
        show_lines=show_lines,
        header_style=header_style,
        border_style=border_style
    )

    for header in headers:
        table.add_column(header, justify=justify)

    for row in rows:
        table.add_row(*[str(cell) for cell in row], style=row_style)

    return table

# 🧱 Build a colored panel
def create_panel(content, title="", style="bold white", border_style="white"):
    return Panel(
        content,
        title=title,
        title_align="center",
        style=style,
        border_style=border_style,
        padding=(1, 2)
    )

from rich.syntax import Syntax

def highlight_code(code: str, language: str = "python", theme: str = "monokai", line_numbers: bool = True):
    """
    Display syntax-highlighted code block using Rich.

    Args:
        code (str): The code to highlight.
        language (str): The language for syntax highlighting.
        theme (str): The theme used by Rich (e.g. "monokai", "dracula").
        line_numbers (bool): Whether to show line numbers.
    """
    syntax = Syntax(code, language, theme=theme, line_numbers=line_numbers)
    print(syntax)

# ================================
# 🧱 Colorful Layout Demonstration
# ================================

def show_layout():
    """Display a colorful side-by-side layout demo using Rich Layout + Panels."""
    from rich.panel import Panel

    layout = Layout()
    layout.split_row(
        Layout(Panel("Left Panel Content", title="Left", border_style="cyan"), name="left"),
        Layout(Panel("Right Panel Content", title="Right", border_style="magenta"), name="right"),
    )
    console.print(layout)

from rich.console import Console
from rich.text import Text
from rich.color import Color

from rich.text import Text
from rich.console import Console
from rich.color import Color

from rich.color import Color

def parse_color_string(color_string):
    if isinstance(color_string, tuple):
        return color_string
    if color_string.startswith("#") and len(color_string) == 7:
        return tuple(int(color_string[i:i+2], 16) for i in (1, 3, 5))
    elif color_string.startswith("rgb("):
        return tuple(map(int, color_string[4:-1].split(",")))
    else:
        try:
            return Color.parse(color_string).triplet
        except:
            return None

from rich.console import Console
from rich.text import Text
from rich.color import Color

# ⬇️ make sure this has access to your colors dictionary!

def parse_color_string(color_string):
    # Step 1: Check in color dictionary
    color_val = colors.get(color_string.lower(), color_string)

    # Step 2: Handle direct tuple
    if isinstance(color_val, tuple):
        return color_val

    # Step 3: Handle #hex
    if isinstance(color_val, str):
        if color_val.startswith("#") and len(color_val) == 7:
            return tuple(int(color_val[i:i+2], 16) for i in (1, 3, 5))
        elif color_val.startswith("rgb("):
            return tuple(map(int, color_val[4:-1].split(",")))

    # Step 4: Try Rich parsing
    try:
        return Color.parse(color_val).triplet
    except Exception:
        return None

def gradient_print(text, color1="cyan", color2="orchid", bold=True):
    start_color = parse_color_string(color1)
    end_color = parse_color_string(color2)

    if start_color is None or end_color is None:
        raise ValueError(f"Unknown color format: {color1}, {color2}")

    console = Console()
    gradient_text = Text(text)
    length = len(gradient_text)

    for i in range(length):
        ratio = i / max(length - 1, 1)
        r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
        color = f"rgb({r},{g},{b})"

        if bold:
            gradient_text.stylize(f"bold {color}", i, i + 1)
        else:
            gradient_text.stylize(color, i, i + 1)

    console.print(gradient_text)

'''

from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from random import choice

console = Console()

__all__ = [
    "fancy_print",
    "with_step_progress",
    "gradient_print",
    "create_panel",
    "rich_table",
    "parse_color_string",
    "colors"
]

# ------------------ Fancy Print ------------------ #
def fancy_print(
    label="",
    value=None,
    label_color="hot_pink",
    label_style="bold",
    value_color="mint_green",
    value_style="italic",
    label_rainbow=False,
    rainbow=False,
    random_style=False,
    random_color=False,
    style=None,
    color=None,
):
    color_keys = list(colors.keys())
    style_options = ["bold", "italic", "underline", "reverse", "dim", "bold italic", "bold underline"]

    if random_color:
        label_color = choice(color_keys)
        value_color = choice(color_keys)

    if random_style:
        value_style = choice(style_options)

    if style:
        value_style = style
        label_style = style

    if color:
        value_color = color
        label_color = color

    label_hex = colors.get(label_color, "#ffffff")
    value_hex = colors.get(value_color, "#ffffff")

    label_text = Text(str(label), style=f"{label_style} {label_hex}")
    value_str = "" if value is None else str(value)
    value_text = Text(value_str, style=f"{value_style} {value_hex}")

    console.print(label_text + value_text)
    return ""

# ------------------ Gradient Print ------------------ #
def gradient_print(text, color1="blue", color2="magenta", bold=True):
    from rich.text import Text
    from rich.color import Color
    from rich.segment import Segment
    from rich.style import Style

    gradient = Text()
    length = len(text)
    for index, char in enumerate(text):
        ratio = index / max(length - 1, 1)
        color = Color.blend(Color.parse(color1), Color.parse(color2), ratio)
        gradient.append(char, style=Style(color=color.get_truecolor().hex, bold=bold))
    console.print(gradient)

# ------------------ Step Progress ------------------ #
def with_step_progress(title="Working...", steps=3, transient=True):
    def wrapper(func):
        def inner(*args, **kwargs):
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TimeElapsedColumn(),
                transient=transient,
            ) as progress:
                task = progress.add_task(title, total=steps)
                result = func(progress=progress, task=task, *args, **kwargs)
                progress.update(task, advance=steps)
                return result
        return inner
    return wrapper

# ------------------ Create Panel ------------------ #
def create_panel(content, title="", border_style="cyan"):
    return Panel(content, title=title, border_style=border_style)

# ------------------ Rich Table ------------------ #
def rich_table(headers, *rows, title="Stocks", title_style="bold cyan"):
    table = Table(title=title, title_style=title_style)
    for header in headers:
        table.add_column(header, style="bold")
    for row in rows:
        table.add_row(*row)
    return table

# ------------------ Parse Color String ------------------ #
def parse_color_string(color_name):
    return colors.get(color_name, "#ffffff")
'''