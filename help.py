# -*- coding: utf-8 -*-                     
import RPi.GPIO as GPIO
import time                            
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)
def main():	
    while True:  
        print("请输入0/1：0--断开开关；1--导通开关\n")
        cmd=int(input())
        if cmd==1:   
            GPIO.output(12, GPIO.LOW)
        elif cmd==0:   
            GPIO.output(12, GPIO.HIGH)
        else:    
            print("输入错误\n")
           
try:
	main()
except KeyboardInterrupt:
    print( "退出")
GPIO.cleanup( )
