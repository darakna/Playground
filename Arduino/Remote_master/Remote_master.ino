```cpp
// Remote Arduino Code – Non-blocking with auto-ack and retries
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define CE_PIN 9
#define CSN_PIN 10
RF24 radio(CE_PIN, CSN_PIN);
const byte address[6] = "00001";

#define LED_PIN 2 // Feedback LED
int ledState = LOW;
unsigned long previousMillisLED = 0;
unsigned long ledBlinkOn = 50, ledBlinkOff = 50;

// Controls (potentiometers)
#define CONTROL1_PIN A0
#define CONTROL2_PIN A1
#define CONTROL3_PIN A2
#define CONTROL4_PIN A3

// Encryption key
const byte key[4] = {0xAA, 0xBB, 0xCC, 0xDD};
byte packet[4];

unsigned long lastSendMillis = 0;
const unsigned long sendInterval = 2; // ~500pps = 2ms interval

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);

  if (!radio.begin()) {
    Serial.println("NRF24 init failed");
  } else {
    radio.setDataRate(RF24_1MBPS);
    radio.setPALevel(RF24_PA_MAX);
    radio.openWritingPipe(address);
    radio.setRetries(3, 15); // retries 3, delay 15*250us
    radio.stopListening();
  }
}

void loop() {
  unsigned long now = millis();

  // ------------------- Read controls -------------------
  int val1 = analogRead(CONTROL1_PIN) / 4; // 0-1023 -> 0-255
  int val2 = analogRead(CONTROL2_PIN) / 4;
  int val3 = analogRead(CONTROL3_PIN) / 4;
  int val4 = analogRead(CONTROL4_PIN) / 4;

  // ------------------- Send packet non-blocking -------------------
  if (now - lastSendMillis >= sendInterval) {
    packet[0] = val1 ^ key[0];
    packet[1] = val2 ^ key[1];
    packet[2] = val3 ^ key[2];
    packet[3] = val4 ^ key[3];

    bool success = radio.write(packet, sizeof(packet));

    // LED feedback
    if (success) {
      ledBlinkOn = 50;
      ledBlinkOff = 50;
    } else {
      ledBlinkOn = 200;
      ledBlinkOff = 100;
    }

    lastSendMillis = now;
  }

  // ------------------- Update LED non-blocking -------------------
  if ((ledState == HIGH && now - previousMillisLED >= ledBlinkOn) ||
      (ledState == LOW && now - previousMillisLED >= ledBlinkOff)) {
    ledState = !ledState;
    digitalWrite(LED_PIN, ledState);
    previousMillisLED = now;
  }
}
```
