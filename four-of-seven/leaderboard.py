import serial
from os import system
from time import sleep


LEADERBOARD_FILE = 'leaderboard.txt'


# I think it is a serial bus.
serial_bus = serial.Serial('COM3', 115200, timeout=0)
times = {}


system('cls')


try:
    while True:
        data = serial_bus.readline().strip().decode('utf-8')
        if data:
            name = input('Name: ')
            system('cls')
            times[name] = int(data)
            with open(LEADERBOARD_FILE, 'a') as leaderboard_file:
                for current_name in sorted(
                        times.keys(),
                        key=lambda names: times[names]
                ):
                    print(current_name, times[current_name])
                leaderboard_file.write(name + ', ' + data + '\n')
            print()
        sleep(2)

except KeyboardInterrupt:
    serial_bus.close()
