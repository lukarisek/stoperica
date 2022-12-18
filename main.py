def on_button_pressed_a():
    global start
    start = input.running_time()
    basic.show_icon(IconNames.YES)
    basic.pause(500)
    basic.show_leds("""
        . # # # .
                # . # . #
                # . . . #
                # . . . #
                . # # # .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global vrijeme, start
    if start != 0:
        vrijeme = Math.round((input.running_time() - start) / 1000)
        basic.clear_screen()
        basic.pause(500)
        basic.show_number(vrijeme)
        basic.pause(2000)
        start = 0
    else:
        basic.clear_screen()
        basic.pause(500)
        basic.show_number(vrijeme)
        basic.pause(2000)
    basic.show_leds("""
        . # # # .
                # . # . #
                # . . . #
                # . . . #
                . # # # .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

vrijeme = 0
start = 0
start = 0
vrijeme = 0
basic.show_leds("""
    . # # # .
        # . # . #
        # . . . #
        # . . . #
        . # # # .
""")