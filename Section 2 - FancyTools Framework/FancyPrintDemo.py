# ╔════════════════════════════════════════════════════════════════════╗
# ║                  ✨ FANCY PRINT DEMO v2 (Full Version)             ║
# ║  This script showcases styled printing using Rich with full       ║
# ║  customization for labels, values, rainbow, random styling, etc.  ║
# ╚════════════════════════════════════════════════════════════════════╝

from rich.console import Console
from rich.text import Text
import random

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
    "aqua": "#00ffff"
}

# 🖌 Style options
style_options = [
    "bold", "italic", "underline", "dim",
    "reverse", "bold italic", "bold underline"
]

# 🌈 Rainbow effect helper

def rainbow_text(text):
    rainbow = Text()
    color_keys = list(colors.values())
    for i, char in enumerate(str(text)):
        rainbow.append(char, style=color_keys[i % len(color_keys)])
    return rainbow

# 💅 Fancy Print Function
def fancy_print(label="", value=None,
                label_color="hot_pink", label_style="bold",
                value_color="mint_green", value_style="italic",
                label_rainbow=False, rainbow=False,
                random_style=False, random_color=False):
    """
    Styled output of label and value using Rich.
    Now supports:
    - Separate styles/colors for label and value
    - Rainbow styling on either label or value
    - Optional random style and/or random color
    """
    color_keys = list(colors.keys())

    if random_color:
        label_color = random.choice(color_keys)
        value_color = random.choice(color_keys)

    label_hex = colors.get(label_color, "#ffffff")
    value_hex = colors.get(value_color, "#ffffff")

    if random_style:
        value_style = random.choice(style_options)

    label_text = rainbow_text(str(label)) if label_rainbow else Text(str(label), style=f"{label_style} {label_hex}")
    value_text = rainbow_text(str(value)) if rainbow else Text(str(value), style=f"{value_style} {value_hex}")

    console.print(label_text + value_text)


# ╭──────────────────────────╮
# │        EXAMPLES          │
# ╰──────────────────────────╯
if __name__ == "__main__":
    # 1. Basic string
    fancy_print("Greeting: ", "Hey babe, you're amazing!", "orchid", "bold")

    # 2. List output
    shopping_list = ["apples", "bananas", "cereal"]
    fancy_print("🛒 Shopping List: ", shopping_list, "mint_green", "bold")

    # 3. Tuple output
    modules = ("Networking", "Cloud", "Python")
    fancy_print("📚 Modules: ", modules, "sky_blue", "italic")

    # 4. Number output
    total_price = 42.99
    fancy_print("💵 Total Price: ", total_price, "gold", "bold")

    # 5. Conditional output
    score = 85
    if score >= 90:
        fancy_print("🏆 Grade: ", "A+", "gold", "bold underline")
    else:
        fancy_print("📉 Grade: ", "Needs work", "crimson", "bold")

    # 6. Rainbow value
    fancy_print("🌈 Message: ", "You are limitless.", rainbow=True)

    # 7. Rainbow label only
    fancy_print("🌟 Self-Worth: ", "Unshakable.", label_rainbow=True, value_color="deep_violet", value_style="bold italic")

    # 8. Random style
    fancy_print("🎲 Random Style: ", "Spin the wheel!", value_color="electric_blue", random_style=True)

    # 9. Mixed data formatting
    nested = [["a", "b"], ["c", "d"]]
    fancy_print("🔁 Nested List: ", nested, label_color="neon_green", label_style="bold", value_color="lime", value_style="dim")

    # 10. [NEW] Random color only
    fancy_print("🎨 Random Colors: ", "Mystery palette engaged!", random_color=True)

    # 11. [NEW] Random color + style
    fancy_print("💫 Full Randomized: ", "Color + Style chaos!", random_color=True, random_style=True)

    # 12. [NEW] Rainbow value with random label color
    fancy_print("🌈 Label Mystery: ", "But the value is rainbow!", rainbow=True, random_color=True)

    # 13. [NEW] Random color + chosen style
    fancy_print("🎯 Targeted Style: ", "Chosen style, surprise color!", value_style="bold italic", random_color=True)

    # 14. [NEW] Random style + chosen color
    fancy_print("🎯 Styled Wildcard: ", "Your color, random vibe!", value_color="orchid", random_style=True)

# ╭──────────────────────────╮
# │     DICTIONARY DEMOS     │
# ╰──────────────────────────╯

# 15. [NEW] Dictionary extraction examples 🧠
profile = {
    "name": "Justin",
    "role": "Cybersecurity Student",
    "language": "Python",
    "emoji": "🧠💻"
}

# Print individual key-value with styling
fancy_print(
    label="🧍 Name: ",
    value=profile["name"],
    label_color="orchid",
    value_color="mint_green",
    value_style="bold"
)

# Print all key-value pairs with consistent style
for key, val in profile.items():
    fancy_print(
        label=f"{key.title()}: ",
        value=val,
        label_color="sky_blue",
        value_color="sunset_orange",
        value_style="italic"
    )

# Print all key-value pairs with random colors/styles
for key, val in profile.items():
    fancy_print(
        label=f"🎲 {key.title()}: ",
        value=val,
        random_color=True,
        random_style=True
    )

# Emojis as label enhancements + rainbow values
emoji_labels = {
    "name": "🧍",
    "role": "🎓",
    "language": "🧠",
    "emoji": "✨"
}

for key, val in profile.items():
    fancy_print(
        label=f"{emoji_labels.get(key, '')} {key.title()}: ",
        value=val,
        rainbow=True,
        label_color="lavender",
        label_style="bold"
    )
