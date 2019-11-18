"""
***USEFUL LINKS***
basic tutrial: https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
movements: https://www.pyimagesearch.com/2019/04/01/pan-tilt-face-tracking-with-a-raspberry-pi-and-opencv/

***PYTHON INSTALLED PACKAGES***
PiCamera >> pip3 install "picamera[array]"
cv2 >> pip3 install opencv-python
face_recognition >> pip3 install face_recognition

"""

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import face_recognition
import os

class Camera():
    def __init__(self):
        # initialize the camera and grab a reference to the raw camera capture
        try:
            self.camera = PiCamera()
        except Exception as e:
            print('Camera doesnt work because :')
            print(e)
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(self.camera, size=(640, 480))
        time.sleep(0.2)

        path = f"image\\child.jpeg"
        if os.path.exists(path):
            image = face_recognition.load_image_file(path)
            self.encoded_child = face_recognition.face_encodings(image)[0]
            print ('encoded succeeded!', self.encoded_child)
        else:
            self.encoded_child = None
            print('There is no image for the child in image directory!!')


    def detect_face(self, image):
        small_frame = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)

        if face_locations:
            if self.encoded_child:
                face_encodings = face_recognition.face_encodings(
                    rgb_small_frame, face_locations)

                for face_encoding,(top, right, bottom, left) in zip(face_encodings,face_locations):
                    # See if the face is a match for the known face(s)
                    matche = face_recognition.compare_faces(
                        self.encoded_child, face_encoding)

                    if match:
                        return (top, right, bottom, left)
                    else:
                        pass
                return None
        else:
            return None





car = Camera()
# capture frames from the camera
for frame in car.camera.capture_continuous(car.rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    loc = car.detect_face(image)
    print(loc)

    # show the frame
    # cv2.imshow("Frame", image)
    # key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    car.rawCapture.truncate(0)