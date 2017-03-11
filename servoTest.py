import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(0)
time.sleep(0.5)
pwm.stop()

def movServo(angle):
    duty = float(angle)/10.0 + 2.5
    #pwm.ChangeDutyCycle(duty)
    pwm.start(duty)
    time.sleep(1)
    pwm.stop()
