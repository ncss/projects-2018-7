# SPI dotstars
# Authors: Sofia, Owen, Moss

from microbit import *
import radio

radio.on()
radio.config(channel = 24)

increment = 1000-28.57
lights = 35
N_LEDS = 35
health = 1000

"""
global rgb


rgb = [(255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0),
       (255, 0, 0)]
"""


def write_frames(frames):
    spi.write(bytes(frames))

def rgb_to_frames(rgb):
    frames = [0]*4

    for r, g, b in rgb:
        frames += [0b11111111, b, g, r]

    frames += [0xff]*4

    return frames

def main(lights):
    spi.init(baudrate=1000000, mosi=pin13, sclk=pin0)
    
    rgb = []
    
    for _ in range(lights):
        rgb.append((0, 255, 0))
    
    for _ in range(35 - lights):
        rgb.append((255, 0, 0))
    
    frames = rgb_to_frames(rgb)
    write_frames(frames)

while True:
    msg = radio.receive()
    if msg:
        try:
            if msg.startswith("player1_health:"):
                health = int(msg.split(":")[1])
                percentage_health = health/1000
                lights = int(percentage_health * N_LEDS)
        except:
            pass
    
    """
    if increment > health:
        while increment > health:
            increment -= 28.57
            lights -= 1
    """
    
    main(lights)
    sleep(50)

    


