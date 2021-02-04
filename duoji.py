#舵机控制python实现
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
servopin=21
GPIO.setup(servopin,GPIO.OUT)
p=GPIO.PWM(servopin,50)
p.start(0)
time.sleep(1)
n=1
while(n<2):
    for i in range(0,360,10):
        p.ChangeDutyCycle(2.5+10.0*i/360)
        time.sleep(0.1)
    n=n+1
GPIO.cleanup()
