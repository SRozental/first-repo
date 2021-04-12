import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

D = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setwarnings(False)
for i in range(len(D)):
    GPIO.setup(D[i] , GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

def decToBinList(decNumber):
    arr = [0 for _ in range(8)]
    if decNumber == 0:
        return arr
    i = 0
    while decNumber != 1:
        arr[i] = decNumber % 2
        decNumber = decNumber // 2
        i += 1
    arr[i] = (decNumber)
    arr.reverse()
    return arr

def lightNumber(number):
    arr = decToBinList(number)
    D = [26, 19, 13, 6, 5, 11, 9, 10]
    for i in range(len(arr)):
        GPIO.output(D[i], arr[i])

def comp():
    while True:
        for i in range(256):
            lightNumber(i)
            time.sleep(0.001)
            if i == 3:
                print()
            if GPIO.input(4)==0:
                print(i*0.0128)
                break
            else:
                continue
    

GPIO.output(17, 1)
comp()