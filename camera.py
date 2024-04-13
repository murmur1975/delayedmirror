import cv2
from baseCamera import BaseCamera
#from detectionSleepiness import DetectionSleepiness

class Camera(BaseCamera):
    tick = 0
    fpsColor = (0, 255, 0)

#    infApp = DetectionSleepiness()

    def __init__(self):
        super().__init__()

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, frame = camera.read()

#            frame = Camera.infApp.getDetectResultFrame(frame)
            yield cv2.imencode('.jpg', Camera.__drawingFps(frame))[1].tobytes()

    @staticmethod
    def __drawingFps(frame):
        fps = 0
        if Camera.tick != 0:
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - Camera.tick)
        Camera.tick = cv2.getTickCount()
        return cv2.putText(frame, "FPS:{} ".format(int(fps)), 
                    (520, 30), cv2.FONT_HERSHEY_DUPLEX, 1, Camera.fpsColor, 1, cv2.LINE_AA)
