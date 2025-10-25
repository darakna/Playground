#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// NRF24 pins
#define CE_PIN 9
#define CSN_PIN 10
RF24 radio(CE_PIN, CSN_PIN);

const byte address[6] = "00001";

// LED feedback
#define LED_PIN LED_BUILTIN
int ledState = LOW;
unsigned long previousMillisLED = 0;
unsigned long ledBlinkOn = 200, ledBlinkOff = 0;

// Motor 1 pins
#define R_EN1 3
#define RPWM1 5
#define L_EN1 4
#define LPWM1 6

// Motor 2 pins
#define R_EN2 7
#define RPWM2 A0
#define L_EN2 8
#define LPWM2 A1

// Encryption key
const byte key[4] = {0xAA, 0xBB, 0xCC, 0xDD};

// Received packet
byte packet[4];
int motor1PWMVal = 127;
int motor2PWMVal = 127;

// Smooth ramp
float currentMotor1 = 127;
float currentMotor2 = 127;
float rampFactor = 0.1;

// Deadzone
const int deadzoneCenter = 127;
const int deadzoneRange = 5;

// Timing
unsigned long lastPacketMillis = 0;
const unsigned long failsafeTimeout = 1000; // 1 second

bool noAntenna = false;

void setBTS7960(int pwmVal, int pwmPinFwd, int pwmPinRev){
  if(abs(pwmVal - deadzoneCenter) <= deadzoneRange){
    analogWrite(pwmPinFwd, 0);
    analogWrite(pwmPinRev, 0);
  } else if(pwmVal > deadzoneCenter){
    analogWrite(pwmPinFwd, map(pwmVal, deadzoneCenter+1, 255, 0, 255));
    analogWrite(pwmPinRev, 0);
  } else {
    analogWrite(pwmPinRev, map(pwmVal, deadzoneCenter-1, 0, 0, 255));
    analogWrite(pwmPinFwd, 0);
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);

  // Motor 1 pins
  pinMode(R_EN1, OUTPUT); pinMode(L_EN1, OUTPUT);
  pinMode(RPWM1, OUTPUT); pinMode(LPWM1, OUTPUT);
  digitalWrite(R_EN1, HIGH); digitalWrite(L_EN1, HIGH);

  // Motor 2 pins
  pinMode(R_EN2, OUTPUT); pinMode(L_EN2, OUTPUT);
  pinMode(RPWM2, OUTPUT); pinMode(LPWM2, OUTPUT);
  digitalWrite(R_EN2, HIGH); digitalWrite(L_EN2, HIGH);

  // NRF24 init
  if (!radio.begin()){
    noAntenna = true;
    Serial.println("NRF24 init failed");
  } else {
    radio.setDataRate(RF24_1MBPS);
    radio.setPALevel(RF24_PA_MAX);
    radio.openReadingPipe(0, address);
    radio.setRetries(3, 15); // retries: 3, delay 15*250us
    radio.startListening();
    noAntenna = false;
  }

  lastPacketMillis = millis();
}

void loop() {
  unsigned long now = millis();

  // ------------------- Receive data -------------------
  if (radio.available()) {
    radio.read(packet, sizeof(packet));
    motor1PWMVal = packet[0] ^ key[0];
    motor2PWMVal = packet[1] ^ key[1];
    lastPacketMillis = now;
  }

  // ------------------- Failsafe -------------------
  if (now - lastPacketMillis > failsafeTimeout){
    motor1PWMVal = deadzoneCenter;
    motor2PWMVal = deadzoneCenter;
  }

  // ------------------- Smooth ramp -------------------
  currentMotor1 += (motor1PWMVal - currentMotor1) * rampFactor;
  currentMotor2 += (motor2PWMVal - currentMotor2) * rampFactor;

  // ------------------- Apply to motors -------------------
  setBTS7960((int)currentMotor1, RPWM1, LPWM1);
  setBTS7960((int)currentMotor2, RPWM2, LPWM2);

  // ------------------- LED feedback -------------------
  if (now - lastPacketMillis <= 50){
    ledBlinkOn = 200;
    ledBlinkOff = 0;
  } else if(noAntenna){
    ledBlinkOn = 100;
    ledBlinkOff = 50;
  } else {
    ledBlinkOn = 0;
    ledBlinkOff = 0;
    digitalWrite(LED_PIN, LOW);
  }

  if ((ledState == HIGH && now - previousMillisLED >= ledBlinkOn) ||
      (ledState == LOW && now - previousMillisLED >= ledBlinkOff)){
    ledState = !ledState;
    digitalWrite(LED_PIN, ledState);
    previousMillisLED = now;
  }
}
