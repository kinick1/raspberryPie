import picamera as pc

with pc.PiCamera() as camera :
    camera.resolution=(640,480)
    camera.start_preview()
    camera.start_recording('video.h264')
    camera.wait_recording(5)
    camera.stop_recording()
    camera.stop_preview()
