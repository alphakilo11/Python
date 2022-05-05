"""morse code for active buzzer or laser emitter"""
#TODO wrap into function morse(dit_length, word_length, high/low)
import time
import RPi.GPIO as GPIO
import encrypt_morse

dit_length = 0.060
word_length = 5
string = "Hello World"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT) #GPIO26 on Pi4b
GPIO.output(37, GPIO.HIGH) #to silence the buzzer
morse_string = encrypt_morse.encrypt(string)

print(morse_string)
time.sleep(5)

for i in morse_string:
    if i == '.':
        GPIO.output(37, GPIO.LOW)
        time.sleep(dit_length)
        GPIO.output(37, GPIO.HIGH)
        time.sleep(dit_length)
        continue
    if i == '-':
        GPIO.output(37, GPIO.LOW)
        time.sleep(dit_length * 3)
        GPIO.output(37, GPIO.HIGH)
        time.sleep(dit_length)
        continue
    if i == ' ':
        time.sleep(dit_length * word_length)
        continue
    
GPIO.cleanup()
print("Finished!")
