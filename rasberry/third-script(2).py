import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
D = [10,9,11,5,6,13,19,26]
for i in D:
    GPIO.setup(i, GPIO.OUT)

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

def num2dac(number):
    X=decToBinList(number%256)
    X.reverse()
    for i in range(8):
        GPIO.setup(D[i],GPIO.OUT)
    for i in range(8):
        GPIO.output(D[i],X[i])
    time.sleep(0.1)
    
def sinToVoltage(amplitude,samplingFrequency):
    for i in amplitude:
        value = int(i)
        X = decToBinList(value%256)
        X.reverse()
        for i in range(8):
            GPIO.setup(D[i],GPIO.OUT)
        for i in range(8):
            GPIO.output(D[i],X[i])
        time.sleep(1/samplingFrequency)

def sinToVoltage2(amplitude,samplingFrequency):
    for i in amplitude:
        value = int(i)
        X = decToBinList(value%256)
        X.reverse()
        for i in range(8):
            GPIO.setup(D[i],GPIO.OUT)
        GPIO.output(D,X)
        time.sleep(1/samplingFrequency)

try:
    trrime = int(input())
    frequency = float(input())
    samplingFrequency = int(input())
    trime = np.arange(0, trrime, float(1/samplingFrequency))
    amplitude = (np.sin((2*3.14*frequency)*trime) +1)*127.5
    print(amplitude)
    sinToVoltage(amplitude,samplingFrequency)
    sinToVoltage2(amplitude,samplingFrequency)
    plt.plot(trime, amplitude)
    plt.title("Синус")
    plt.xlabel("Время")
    plt.ylabel("Амплитуда sin(time)")
    plt.show()
finally:
    for i in range(8):
        GPIO.output(D[i],0)
    GPIO.cleanup()       