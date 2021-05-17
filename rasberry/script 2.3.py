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

def bin_search(left, right):
    while right - left > 1:
        i= (left + right)//2
        lightNumber(i)
        time.sleep(0.01)
        if GPIO.input(4) == 0:
            right = i
        else:
            left = i
        left, right = bin_search(left, right)
    return left,right

try:
    prev =-1
    while True:
        left, right = bin_search(left = 0,right = 256)
        i = left
        if i != prev:
            prev = i
            analog = i*3.2/251
            print("Digital value:", i, ", Analog value:", round(analog, 2),"V")
finally:
    GPIO.setup(D, GPIO.OUT)
    GPIO.output(D,0)


GPIO.output(17, 1)