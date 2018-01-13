from microbit import *


# If any sensor is seeing brighted (lower) than this, it can be considered on.
THRESHOLD = 590
# If red and green are on, that is white, if they are both off, that is red.
RED_PIN = pin1
GREEN_PIN = pin2


detected_colour = lambda pin: pin.read_analog() < THRESHOLD
on_red = lambda: detected_colour(RED_PIN) and not detected_colour(GREEN_PIN)
on_green = lambda: detected_colour(GREEN_PIN) and not detected_colour(RED_PIN)
on_white = lambda: detected_colour(GREEN_PIN) and detected_colour(RED_PIN)


order = [on_red, on_green, on_white]
position_in_order = 0

while True:
    print(position_in_order)
    if position_in_order < len(order) and order[position_in_order]():
        position_in_order += 1
    if position_in_order >= len(order):
        print("Finished")

    if button_a.was_pressed():
        position_in_order = 0
