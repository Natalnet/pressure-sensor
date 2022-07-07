from math import pi, pow 
from machine import Pin, ADC #ADC let you do a analog read
from time import sleep #sleep is a delay for python
fsr_Pin = ADC(Pin(36))  #The minimum value is 0 and the maximum is 4095
#GPIOs only input are 34, 35, 36 and 39


CV_CONDUCTANCE = 1000000 #the necessary value to calculate the conductance later (in microMhos)
DIAMETER_FSR = 0.0127 #diameter of the active section of the fsr (meter).


tension_fsr = -1 #the analog reading in voltage.
conductance = -1
resistance_fsr = -1 #the voltage converted into resistance.
force_newton = -1 #the resistance converted to Newton.
pressure_pascal = -1 #the pressure made converted to Pascal.
mass_kg = -1 #the force(N) converted to mass(kg).
area_fsr = 0


#According to the formula Rfsr = [(V - Vfsr) * R] / Vfsr:
V = 3300 #Supply voltage of ESP32
R = 10000 #Resistance of the pull-down resistor.


def read():
    global fsr_read
    fsr_read = fsr_Pin.read()
    sleep(0.1)


def map():
    global tension_fsr
    #Scale the resistence value between 0 and 4095 to 0 and 3300.
    in_min = 0
    in_max = 4095
    out_min = 0
    out_max = 3300
        
    tension_fsr = ((fsr_read - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def calculos():
    global V, R, resistance_fsr, conductance
    resistance_fsr = ((V - tension_fsr)*R) / tension_fsr
    conductance = 1000000 / resistance_fsr


def newton():
    global conductance, force_newton
    if (conductance <= 1000):
        force_newton = conductance/80
    else:
        force_newton = (conductance - 1000)/30


def pascal():
    global radius, area_fsr, pressure_pascal, force_newton
    #Converting to Pascal. Pa = force / area.
    #the sensor's active area is a circle, so it may be found using area = pi*(radius)².
    radius = DIAMETER_FSR/2
    area_fsr = pi * pow(radius, 2)
    pressure_pascal = force_newton / area_fsr


while True:
    print("Força em Newtons: \n")
    print("Força em Pascal: \n")
