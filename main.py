from machine import Pin 
import bluetooth
from ble_simple_peripheral import BLESimplePeripheral
import time

ble = bluetooth.BLE()
led = Pin("LED", Pin.OUT)
led.value(1)
# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)
led = ("LED", pin.OUT)
# Create a Pin object for the onboard LED, configure it as an output
pins = {
    "GP2": Pin(2, Pin.OUT),  # Example: LED1 on GPIO2
    "GP3": Pin(3, Pin.OUT),
    "GP4": Pin(4, Pin.OUT),  # Example: LED2 on GPIO4
    "GP5": Pin(5, Pin.OUT),   # Example: LED3 on GPIO5
    "GP6": Pin(6, Pin.OUT),
    "GP7": Pin(7, Pin.OUT),
    "GP8": Pin(8, Pin.OUT),
    "GP9": Pin(9, Pin.OUT),
    "GP10": Pin(10, Pin.OUT),
    "GP11": Pin(11, Pin.OUT),
    "GP12": Pin(12, Pin.OUT),
    "GP13": Pin(13, Pin.OUT),
    "GP14": Pin(14, Pin.OUT),
    "GP15": Pin(15, Pin.OUT),
    "GP16": Pin(16, Pin.OUT),
    "GP17": Pin(17, Pin.OUT),
    "GP18": Pin(18, Pin.OUT),
    "GP19": Pin(19, Pin.OUT),
    "GP20": Pin(20, Pin.OUT),
    "GP21": Pin(21, Pin.OUT),
    "GP22": Pin(22, Pin.OUT),
    "GP23": Pin(23, Pin.OUT),
    "GP24": Pin(24, Pin.OUT),
    "GP25": Pin(25, Pin.OUT),
    "GP26": Pin(26, Pin.OUT),
    "GP27": Pin(27, Pin.OUT),
    "GP28": Pin(28, Pin.OUT),
}

# Initialize the LED state to 0 (off)
led_state = 0\
def led_blink():
    with(True):
        led.value(not led.value())
        time.sleep(1)

# Callback function to handle received BLE data
def on_rx(data):
    command = data.decode().strip()  # Decode bytes to string and remove extra spaces/newlines
    print("Data received:", command)

    # Split command to identify action and target pin
    parts = command.split("_")
    if len(parts) != 2:
        print("Invalid command format. Use: TOGGLE_GP2, ON_GP4, OFF_GP5")
        return
    
    action, pin_name = parts[0], parts[1]

    if pin_name in pins:
        if action == "Toggled":
            pins[pin_name].value(not pins[pin_name].value())  # Toggle pin state
            print(f"Toggled {pin_name}")

        elif action == "ON":
            pins[pin_name].value(1)  # Turn ON the pin
            print(f"{pin_name} turned ON")

        elif action == "OFF":
            pins[pin_name].value(0)  # Turn OFF the pin
            print(f"{pin_name} turned OFF")
    
    else:
        print(f"Invalid pin name: {pin_name}")
# Start an infinite loop
while True:
    if sp.is_connected():  # Check if a BLE connection is established
        sp.on_write(on_rx)  # Set the callback function for data reception
        sp.on_write(led_blink)
Code
