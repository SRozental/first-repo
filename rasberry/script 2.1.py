import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

D = [26, 19, 13, 6, 5, 11, 9, 10]
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

GPIO.output(17, 1)
while True:
    print("enter value")
    n = int(input())
    if n == -1:
        print("the end")
        break
    