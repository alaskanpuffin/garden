from gpiozero import OutputDevice, Button
from signal import pause

fanButton = Button(23, hold_time=2)
waterButton = Button(24, hold_time=2)

fanRelay = OutputDevice(15)
waterRelay = OutputDevice(18)

def toggleFan():
    print("Toggle Fan")
    fanRelay.toggle()

def toggleWater():
    print("Toggle Water")
    waterRelay.toggle()

def pushButton():
   print("Toggle 2 Extra")

fanButton.when_held = toggleFan
waterButton.when_held = toggleWater


pause()
