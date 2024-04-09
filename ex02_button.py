import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setup(21,gp.IN)
gp.setup(18,gp.OUT)

try:
    while True:
        btn=gp.input(21)
        print(btn)
        if btn==1:
            gp.output(18,gp.HIGH)
        else:
            gp.output(18,gp.LOW)

except KeyboardInterrupt:
    gp.cleanup()