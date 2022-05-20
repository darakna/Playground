import RPi.GPIO as GPIO #Import the GPIO library
import time #Used for waiting between beeps


speakerPin = 22 #Use GPIO numbers for Python, not pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(speakerPin,GPIO.OUT) #Sets the speakerPin as an output pin
n=100    
while(n):
    n=n-1
    GPIO.output(speakerPin,GPIO.HIGH) #Turns the speaker ON
    time.sleep(0.2) #waits a second
    GPIO.output(22,GPIO.LOW) #Turns the speaker OFF
