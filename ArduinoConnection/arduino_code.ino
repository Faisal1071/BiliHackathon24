#include <math.h>

const byte numPins = 8;
byte pins[] = {9, 8, 7, 6, 5, 4, 3, 2};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
}

void loop() {
  const double REFERENCE_VOLTAGE = 5.0; // Reference Voltage of the Arduino
  const int REFERENCE_RESISTANCE = 10000; // Reference Resistance of the Arduino
  const double REFERENCE_TEMPERATURE = 25 + 273.15; // Reference Temperature in Kelvin
  const int B_VALUE = 3950; // Temperature Sensitivity
  const double CORRECTION = -1.0;

  double measuredValue = analogRead(0);
  double measuredVoltage = (measuredValue / 1023) * REFERENCE_VOLTAGE;
  double measuredResistance = measuredVoltage / (REFERENCE_VOLTAGE - measuredVoltage) * REFERENCE_RESISTANCE;
  double measuredTemperature = 1 / (log(measuredResistance / REFERENCE_RESISTANCE) / B_VALUE + 1 / REFERENCE_TEMPERATURE) - 273.15 + CORRECTION;
  int temperatureInteger = int(measuredTemperature);
  Serial.println(measuredTemperature);

  for (byte i = 0; i < numPins; i++) {
    byte state = bitRead(temperatureInteger, i);
    digitalWrite(pins[i], state);
    Serial.print(state);
  }
  Serial.println();

  delay(1000);
}
