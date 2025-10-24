// Definim LED-ul integrat
const int LED_PIN = LED_BUILTIN;

void setup() {
  pinMode(LED_PIN, OUTPUT); // configurare pin ca OUTPUT
}

void loop() {
const int start_duration = 100;
const int stop_duration = 50;


    digitalWrite(LED_PIN, HIGH); // aprinde LED
    delay(start_duration);
    digitalWrite(LED_PIN, LOW);  // stinge LED
    delay(stop_duration);           // pauza între simboluri

}