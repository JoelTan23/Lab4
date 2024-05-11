from time import sleep
from hal import hal_input_switch as hal_is # import hal.hal_input switch as hal_is
from hal import hal_led as led # import hal.hal_led as led
import time
import socket

def LED_Freq(ret):

    led.init()
    start_time = time.time()  # Records the start time

    while time.time() - start_time < 5:  # Run the loop for 5 seconds --> Aided from Google 

        if ret == 1:

            led.set_output(0, 1)
            time.sleep(0.2)
            led.set_output(0, 0)
            time.sleep(0.2)


        else:

            led.set_output(0, 1)
            time.sleep(0.1)
            led.set_output(0, 0)
            time.sleep(0.1)

    led.set_output(0, 0)  # Turn off the LED after 5 seconds


def main():
#Main Code Below
    hal_is.init()
    result = hal_is.read_slide_switch()
    time.sleep(1)

    # Get IP address
    local_ip_address = socket.gethostbyname("raspberrypi")

    LED_Freq(result)


