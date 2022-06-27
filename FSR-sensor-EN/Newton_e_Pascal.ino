#include <math.h>

#define fsr_PIN A0 

int readSensor;
int tension_fsr; // the analog reading in voltage.
unsigned long resistance_fsr; // the voltage converted into resistance.
unsigned long conductance = 1000000; // the opposite of resistance (in microMhosthe)
long force_newton; // the resistance converted to Newton.
long pressure_pascal; // the pressure made converted to Pascal.
long mass_kg; // the force(N) converted to mass(kg).
float diameter_fsr = 12.7; // diameter of the active section of the fsr (square milimiter).
float area_fsr;

void setup(){
  Serial.begin(9600);
}

void loop(){
  // Reading of the sensor
  readSensor = analogRead(fsr_PIN);

  // Converting analog signal to milliVolts .Once the analog signal is between 0 ~1023 and Vcc is between 0 ~5V, those are the arguments used inside the function map
  tension_fsr = map(readSensor, 0, 1023, 0, 5000);

  // According to the formula Rfsr = [(V - Vfsr) * R] / Vfsr:
  int V = 5000; // Supply voltage of Arduino.
  int R = 10000; // Resistance of the pull-down resistor.

  resistance_fsr = ((5000 - tension_fsr)*10000) / tension_fsr;

  // Conductance must be in microMhos, it means G = (1/R) * 1.000.000.
  conductance = conductance / resistance_fsr;

  // Following the graphics and references [3] e [4], we use conductance to approximate force in Newton
  if (conductance <= 1000){
    force_newton = conductance / 80;
  } else {
    force_newton = (conductance - 1000) / 30;
  }

  // Converting to Pascal. Pa = force / area.
  // the sensor's active area is a circle, so it may be found using area = pi*(radius)².
  float radius = diameter_fsr/2;
  area_fsr = M_PI * pow(radius, 2);
  pressure_pascal = force_newton / area_fsr;

  Serial.print("Forca em Newton: ");
  Serial.println(force_newton);
  Serial.print("Pressao em Pascal: ");
  Serial.println(pressure_pascal);
}