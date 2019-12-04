import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 16
GPIO_ECHO = 18

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

def distance():
    count = 0
    GPIO.output(GPIO_TRIGGER,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)
    StartTime = time.time()
    StopTime = time.time()
    
    print(GPIO.input(GPIO_ECHO))
    while GPIO.input(GPIO_ECHO) == 0:
        count+=1
        StartTime = time.time()
        if count>25:
            return -1
    while GPIO.input(GPIO_ECHO)==1:
        StopTime = time.time()
    
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed*34300)/2
    if distance>100:
        return -1
    return distance
    
    '''try:
        while True:
            dist = distance()
            print("Measured Distance = ", dist)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measured stopped by User")
        GPIO.cleanup()
  '''
  
