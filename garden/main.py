from gpiozero import OutputDevice, Button
from signal import pause

fanButton = Button(22, hold_time=2)

fanRelay = OutputDevice(16)


def toggleFan():
    fanRelay.toggle()

fanButton.when_held = toggleFan

pause()
