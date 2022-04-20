import tkinter as tk
from tkinter import ttk

def create_button(width, height, font, background, font_color, text, command, position):
    btn = tk.Button(
        text=text,
        background=background,
        width=width,
        height=height,
        font=font,
        foreground=font_color,
        command=command,
    )
    btn.place(x=position[0], y=position[1])
    return btn


def create_label(font, font_color, text, position, background):
    label = tk.Label(
        text=text,
        font=font,
        foreground=font_color,
        justify=tk.LEFT,
        background=background
    )
    label.place(x=position[0], y=position[1])
    return label

def create_entry(width, font, font_color, position):
    entry = tk.Entry(
        width=width,
        font=font,
        foreground=font_color,
    )
    entry.place(x=position[0], y=position[1])
    return entry


def create_combo_box(width, font, font_color, position, values, default=0, callback=None):
    combo = ttk.Combobox(
        width=width,
        font=font,
        foreground=font_color,
        values=values,
        state="readonly",
    )
    combo.bind("<<ComboboxSelected>>", callback)
    combo.current(default)
    combo.place(x=position[0], y=position[1])
    return combo


