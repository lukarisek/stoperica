input.onButtonPressed(Button.A, function () {
    start = input.runningTime()
    basic.showIcon(IconNames.Yes)
    basic.pause(500)
    basic.showLeds(`
        . # # # .
        # . # . #
        # . . . #
        # . . . #
        . # # # .
        `)
})
input.onButtonPressed(Button.B, function () {
    if (start != 0) {
        vrijeme = Math.round((input.runningTime() - start) / 1000)
        basic.clearScreen()
        basic.pause(500)
        basic.showNumber(vrijeme)
        basic.pause(2000)
        start = 0
    } else {
        basic.clearScreen()
        basic.pause(500)
        basic.showNumber(vrijeme)
        basic.pause(2000)
    }
    basic.showLeds(`
        . # # # .
        # . # . #
        # . . . #
        # . . . #
        . # # # .
        `)
})
let vrijeme = 0
let start = 0
start = 0
vrijeme = 0
basic.showLeds(`
    . # # # .
    # . # . #
    # . . . #
    # . . . #
    . # # # .
    `)
