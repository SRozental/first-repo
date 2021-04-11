import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import numpy
import matplotlib.pyplot as plt


GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

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
    
def sinus(time, freq, samplFreq):
    global D
    i = 0
    ndarray = []
    while i <= time:
        ndarray.append(i*freq)
        i += 1/samplFreg
    for j in range(len(ndarray)):
        ndarray[j] = 2*numpy.pi*freq*ndarray[j]
    y = numpy.sin(ndarray)
    for k in range(len(y)):
        y[k] =(y[k] + 1)*1.65 
        for p in range(len(ndarray)):
            lightNumber(round(y[k]*256/3.3))
            time.sleep(1/samplFreq)
    for elem in D:
        GPIO.setup(elem, GPIO.OUT)
        GPIO.output(elem, 0)  
    return x,y
        

time = float(input())
freq = int(input())
samplFreq=int(input())
x,y=sinus(time,frequancy,samplFreq)
plt.plot(x,y)
plt.show()


D = [26, 19, 13, 6, 5, 11, 9, 10]
for i in D:
    GPIO.output(i, 0)
GPIO.cleanup()       