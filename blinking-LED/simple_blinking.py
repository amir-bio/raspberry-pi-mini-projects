import RPi.GPIO as GPIO
import time

LED_pin = 11
sleep_interval = 1


def setup():
    # numbers pins by physical location
    GPIO.setmode(GPIO.BOARD)
    # set pin mode as output and start in high voltage (LED off)
    GPIO.setup(LED_pin, GPIO.OUT, initial=GPIO.HIGH)


def loop():
    while True:
        print('led on')
        GPIO.output(LED_pin, GPIO.LOW)
        time.sleep(sleep_interval)
        print('led off')
        GPIO.output(LED_pin, GPIO.HIGH)
        time.sleep(sleep_interval)


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print('Cleaning up...')
        # turn LED off
        GPIO.output(LED_pin, GPIO.HIGH)
        GPIO.cleanup()
        print('Done')
