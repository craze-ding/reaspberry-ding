import ptvsd
ptvsd.enable_attach()
ptvsd.wait_for_attach()
ptvsd.break_into_debugger()
import RPi.GPIO as GPIO
import time                
GPIO.setmode(GPIO.BCM)     
GPIO.setup(18,GPIO.OUT)
 
print("PC ON: PC-ON")   
print("Exit: Q and q")
 
while True:
    user_choice=input("Choice:")
    if user_choice=="PC-ON":
          GPIO.output(18,GPIO.HIGH)
          print("3")
          time.sleep(1.0)
          print("2")
          time.sleep(1.0)
          print("1")
          time.sleep(1.0)          
          GPIO.output(18,GPIO.LOW)
    elif user_choice=="q" or user_choice=="Q":
          GPIO.cleanup()