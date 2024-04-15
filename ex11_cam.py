import picamera as pc
import time


camera=pc.PiCamera() 
camera.start_preview()
time.sleep(2)
    for i in range(3):
    camera.capture(f'jun{i}.png')
    time.sleep(1)
camera.stop_preview()
camera.close()
