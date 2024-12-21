from random import choice
import os


with open("lesson_7/lines.txt", "r") as f:
    lines = f.read().splitlines()
    if len(lines) > 0:
        random_line = choice(lines).strip()
        print(random_line)