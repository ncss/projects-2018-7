from microbit import *

uart.init(115200)
send=b''
while True:
    if uart.any():
        x = uart.readall()
        display.scroll(x)
        if x == b'#':            
            display.scroll(send)
            send = b''
        else:
            send+=x

        