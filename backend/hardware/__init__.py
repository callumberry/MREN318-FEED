import threading

from .servoControl import move_servo_min_to_max
from .ledControl import toggle_led
from .stepper import move_stepper_motor
from .lcd import tryWriteToLCD
from .analog import tryGetAnalog
from .encoder import tryGetEncoderData
# from .camera import VideoCamera

encoderThread = threading.Thread(target=tryGetEncoderData)
analogThread = threading.Thread(target=tryGetAnalog)
lcdThread = threading.Thread(target=tryWriteToLCD)
encoderThread.start()
analogThread.start()
lcdThread.start()
