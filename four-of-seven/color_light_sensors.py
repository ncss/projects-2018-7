from microbit import *

order = ['Red', 'White', 'Green']
status = {'Red': False,
        'White': False,
        'Green': False}

Range = {'Red':[600, 630], 
        'White': [500, 530],
        'Green': [400, 430]}
    
while True:
    light_1 = pin1.read_analog()
    light_2 = pin2.read_analog()
    print('red:' + str(light_1))
    print('green:' + str(light_2)) 
    sleep(500)
    
    for color, colRange in Range.items(): 
        if light_1 > colRange[0] and light_1 < colRange[1] and light_2 > colRange[0] and light_2 < colRange[1]: 
            
            status [color] = True 
            

def is_passed(currentColor):
    currentInd = currentcolor
    
    '''
    if light_1 > Red[0] and light_1 < Red[1] and light_2 > Red[0] and light_2 < Red[1]: 
        status ['Red'] = True 
        
    if light_1 > White[0] and light_1 < White[1] and light_2 > White[0] and light_2 < White[1]: 
        status ['White'] = True 
    
    if light_1 > Green[0] and light_1 < Green[1] and light_2 > Green[0] and light_2 < Green[1]: 
        status ['Green'] = True 
        
    
    #if light > 500
        counter =+ 1 
    #else 
        display.show(Image.SAD)
    
    #if light < XXX
    '''
    