#include <Wire.h>
#include <TEA5767N.h>

TEA5767N radio = TEA5767N();

void setup() {
  Serial.begin(9600);
  Wire.begin();

  Serial.println("START");

  radio.selectFrequency(89.1);

  delay(2000);

  Serial.print("Frequency: ");
  Serial.print(radio.readFrequencyInMHz(), 1);
  Serial.println(" MHz");

  Serial.print("Signal level: ");
  Serial.println(radio.getSignalLevel());

  Serial.print("Stereo: ");
  Serial.println(radio.isStereo() ? "YES" : "NO");

  Serial.println("DONE");
}

void loop() {
}
