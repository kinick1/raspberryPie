import spidevRead as sr
import time
import led18 as led

try:
    while True:
        read=sr.analog_read(0)
        print(f'Data : {read}')
        time.sleep(0.5)
        if read<=30:
            led.led_on()
        else:
            led.led_off()
except KeyboardInterrupt:
    led.led_cleanup()
