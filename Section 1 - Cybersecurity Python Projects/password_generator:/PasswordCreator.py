#!/usr/bin/env python3
# 🔐 Ultimate Password Generator (Fancy Style)

import random
import string
from fancytools.fancy import fancy_print, colors
from rich.console import Console
from rich.text import Text

console = Console()

# 🔷 Header
fancy_print("🔐 Welcome to the Ultimate Password Generator! 🔐", label_rainbow=True)

# 🔢 Ask for length
while True:
    try:
        fancy_print("📏 Enter desired password length (4–300):", random_color=True, random_style=True)
        length = int(input("> "))
        if 4 <= length <= 300:
            break
        else:
            fancy_print("❗ Please choose a number between 4 and 300.", random_color=True)
    except ValueError:
        fancy_print("❗ Please enter a valid number.", random_color=True)

# 🔘 Options
def ask(prompt):
    fancy_print(prompt, random_color=True, random_style=True)
    return input("> ").strip().lower() == 'y'

use_upper = ask("🔡 Include uppercase letters? (Y/N):")
use_lower = ask("🔠 Include lowercase letters? (Y/N):")
use_digits = ask("🔢 Include numbers? (Y/N):")
use_symbols = ask("💥 Include symbols? (Y/N):")
exclude_similar = ask("🔎 Exclude similar characters (i, l, 1, |, etc)? (Y/N):")
exclude_ambiguous = ask("🚫 Exclude ambiguous characters ({}[]()/\\'\"`~,;:.<>?)? (Y/N):")
first_char_must_be_letter = ask("🔤 Ensure first character is a letter? (Y/N):")
multi_generate = ask("🎲 Generate multiple password options? (Y/N):")

num_passwords = 1
if multi_generate:
    fancy_print("🔢 How many passwords to generate?", random_color=True, random_style=True)
    try:
        num_passwords = int(input("> "))
    except:
        num_passwords = 3

# 🧪 Build character pool
characters = ''
if use_upper:
    characters += string.ascii_uppercase
if use_lower:
    characters += string.ascii_lowercase
if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

# 🧹 Apply exclusions
if exclude_similar:
    for c in "il1LoO0|":
        characters = characters.replace(c, '')
if exclude_ambiguous:
    for c in "{}[]()/\\'\"`~,;:.<>":
        characters = characters.replace(c, '')

if not characters:
    fancy_print("❌ No valid characters remaining. Exiting.", random_color=True)
    exit()

# 🔑 Generate passwords
fancy_print("\n🧠 Generated Passwords:", "\n", label_rainbow=True)
for _ in range(num_passwords):
    if first_char_must_be_letter:
        letters = string.ascii_letters
        valid_letters = [c for c in letters if c in characters]
        if not valid_letters:
            fancy_print("⚠️ No valid letters available for first character. Exiting.", random_color=True)
            exit()
        first = random.choice(valid_letters)
        rest = ''.join(random.choice(characters) for _ in range(length - 1))
        pwd = first + rest
    else:
        pwd = ''.join(random.choice(characters) for _ in range(length))
    fancy_print(f"💥 {pwd} \n", random_color=True, random_style=True)

