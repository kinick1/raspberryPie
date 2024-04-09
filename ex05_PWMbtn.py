import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(21,gp.IN)
gp.setup(18,gp.OUT)

p= gp.PWM(18,500)
p.start(0)
cnt=0
check=True
# try:
#     while True:
#         btn=gp.input(21)
#         
#         if btn==1:
#             if cnt==0:
#                 p.ChangeDutyCycle(10)
#                 cnt+=1
#             elif cnt==1:
#                 p.ChangeDutyCycle(40)
#                 cnt+=1
#             else :
#                 p.ChangeDutyCycle(80)
#                 cnt=0

try:
    while True:
        btn=gp.input(21)
        
        if btn==1:
            if check== True:
                cnt+=1
                check=False
                
        else:
            check=True
            gp.output(18,cnt%2)
            
        if cnt%3==0:
            p.ChangeDutyCycle(10)
        elif cnt%3==1:
            p.ChangeDutyCycle(40)
        else :
            p.ChangeDutyCycle(80)

except KeyboardInterrupt:
    gp.cleanup()