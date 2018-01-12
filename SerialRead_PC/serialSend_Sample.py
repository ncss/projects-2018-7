from microbit import *

DELAY = 100
FLASH_TIME_MS = 500

f_time = 0
button_list = [False,False]


while True:
  now = running_time()

  #if there is any previously pressed button
  if True in button_list:
    #if button A pressed
    if button_a.was_pressed():
      button_list[0] = True

    #if button B pressed
    if button_b.was_pressed():
      button_list[1] = True

  #if there is no previously pressed button
  else:
    button_list[0] = button_a.was_pressed()
    button_list[1] = button_b.was_pressed()

    #store time when the first button is pressed only when 
    f_time = now  

  #calculate interval time between first and current button pressed.
  difference = now - f_time

  #if difference is higher (longer) than allowed delay
  if difference > DELAY:   
    #if both button is pressed
    if button_list.count(True) == 2:
      display.show('c', delay=FLASH_TIME_MS, wait=False, clear=True)
      print('c')
      #clear the button list
      button_list = [False,False]

    #if only A button is pressed      
    elif button_list[0]:
      display.show('a', delay=FLASH_TIME_MS, wait=False, clear=True)
      print('a')
      #clear the button list
      button_list = [False,False]

    #if only B button is pressed      
    elif button_list[1]:
      display.show('b', delay=FLASH_TIME_MS, wait=False, clear=True)
      print('b')
      #clear the button list
      button_list = [False,False]