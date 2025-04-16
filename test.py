#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: 2023 Kent Gibson <warthog618@gmail.com>

"""Minimal example of toggling a single line."""

"""Minimal example of reading the info for a chip."""

import gpiod

"""
def get_chip_info(chip_path):
    with gpiod.Chip(chip_path) as chip:
        info = chip.get_info()
        print("{} [{}] ({} lines)".format(info.name, info.label, info.num_lines))


if __name__ == "__main__":
    try:
        get_chip_info("/dev/gpiochip1")
    except OSError as ex:
        print(ex, "\nCustomise the example configuration to suit your situation")

"""

import gpiod
import time

from gpiod.line import Direction, Value


def toggle_value(value):
    if value == Value.INACTIVE:
        return Value.ACTIVE
    return Value.INACTIVE


def toggle_line_value(chip_path, line_offset):
    value_str = {Value.ACTIVE: "Active", Value.INACTIVE: "Inactive"}
    value = Value.ACTIVE

    with gpiod.request_lines(
        chip_path,
        consumer="toggle-line-value",
        config={
            line_offset: gpiod.LineSettings(
                direction=Direction.OUTPUT, output_value=value
            )
        },
    ) as request:
        
        print("{}={}".format(line_offset, value_str[value]))
        time.sleep(1)
        value = toggle_value(value)
        request.set_value(line_offset, value)


if __name__ == "__main__":
    #pins=[10,0,20]
    pins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for i in range(0,100):
        try:
            toggle_line_value("/dev/gpiochip0", i)
        except OSError as ex:
            print(ex, "\nCustomise the example configuration to suit your situation")
