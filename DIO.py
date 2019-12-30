from enum import Enum

class __DIO_PRIVATE_PINS(Enum):
    GPIO_2 = 3
    GPIO_3 = 5
    GPIO_4 = 7
    GPIO_14 = 8  # RX
    GPIO_15 = 10 # TX
    GPIO_17 = 11
    GPIO_18 = 12
    GPIO_27 = 13
    GPIO_22 = 15
    GPIO_23 = 16
    GPIO_24 = 18
    GPIO_10 = 19
    GPIO_9 = 21
    GPIO_25 = 22
    GPIO_11 = 23
    GPIO_8 = 24
    GPIO_7 = 26

defaultPins = __DIO_PRIVATE_PINS
class DIO_PINS(Enum):
    SERVO_1 = defaultPins.GPIO_2.value
    SERVO_2 = defaultPins.GPIO_3.value
    SERVO_3 = defaultPins.GPIO_4.value
    SERVO_4 = defaultPins.GPIO_17.value
    SERVO_5 = defaultPins.GPIO_27.value
    SERVO_6 = defaultPins.GPIO_22.value
    SERVO_7 = defaultPins.GPIO_10.value
    MIC_LED = defaultPins.GPIO_9.value
