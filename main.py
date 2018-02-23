from digitalio import DigitalInOut, Direction, Pull
import audioio
import board
import touchio
import neopixel
import time

touch4 = touchio.TouchIn(board.A4)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0,0,0))
pixels.show()

# enable the speaker
spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = Direction.OUTPUT
spkrenable.value = True

delay = 1.400

GREEN = (0, 0x10, 0)
RED = (0x10, 0, 0)
OFF = (0,0,0)

pixels[9] = GREEN
pixels[8] = GREEN
pixels[5] = RED
pixels[6] = RED


def play_file(filename):
    print("playing file "+filename)
    f = open(filename, "rb")
    a = audioio.AudioOut(board.A0, f)
    a.play()
    while a.playing:
        pass
    print("finished")


def pause():
    time.sleep(delay)
    if touch4.value:
        print("A4 touched!")
        play_file("vader.wav")


while True:
    pixels[0] = RED
    pixels[2] = RED
    pixels[4] = RED
    pause()
    pixels[2] = OFF
    pause()
    pixels[0] = OFF
    pixels[4] = OFF
    pixels[2] = RED
    pause()
    pixels[0] = RED
    pause()
    pixels[2] = OFF
    pause()
    pixels[2] = RED
    pause()
    pixels[2] = OFF
    pixels[4] = RED
    pause()
    pixels[0] = OFF
    pixels[2] = RED
    pause()




