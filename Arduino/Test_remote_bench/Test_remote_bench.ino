```cpp
// Remote Test Sketch – Sends incremental PWM values to Car Arduino
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define CE_PIN 9
#define CSN_PIN 10
RF24 radio(CE_PIN, CSN_PIN);

const byte address[6] = "00001";

// Encryption key
const byte key[4] = {0xAA, 0xBB, 0xCC, 0xDD};

byte packet[4];
int value1 = 0;
int value2 = 0;
int increment = 5;

#define LED_PIN 2 // Feedback LED

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);

  if (!radio.begin()) {
    Serial.println("NRF24 init failed");
  } else {
    radio.setDataRate(RF24_1MBPS);
    radio.setPALevel(RF24_PA_MAX);
    radio.openWritingPipe(address);
    radio.stopListening();
    Serial.println("NRF24 ready");
  }
}

void loop() {
  // Increment values for test
  value1 += increment;
  if (value1 > 255 || value1 < 0) increment = -increment;
  value2 += increment;

  // Apply XOR encryption
  packet[0] = value1 ^ key[0];
  packet[1] = value2 ^ key[1];
  packet[2] = 0 ^ key[2];
  packet[3] = 0 ^ key[3];

  // Send packet
  bool success = radio.write(packet, sizeof(packet));

  // Feedback LED
  if (success) {
    digitalWrite(LED_PIN, HIGH);
    delay(50);
    digitalWrite(LED_PIN, LOW);
  } else {
    // If failed, blink longer
    digitalWrite(LED_PIN, HIGH);
    delay(200);
    digitalWrite(LED_PIN, LOW);
  }

  Serial.print("Motor1 PWM: "); Serial.print(value1);
  Serial.print("  Motor2 PWM: "); Serial.println(value2);

  delay(100); // 10Hz test rate
}
```
