# Imports
import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
# from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from keyboard_layout_win_es import KeyboardLayout

keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)
layout = KeyboardLayout(keyboard)

btn1_pin = board.GP0
btn2_pin = board.GP1
btn3_pin = board.GP2
btn4_pin = board.GP3
btn5_pin = board.GP4
btn6_pin = board.GP5
btn7_pin = board.GP6
btn8_pin = board.GP7
btn9_pin = board.GP8
btn10_pin = board.GP9
btn11_pin = board.GP10
btn12_pin = board.GP11

led1_pin = board.GP13
led2_pin = board.GP14
led3_pin = board.GP16
led4_pin = board.GP17
led5_pin = board.GP18
led6_pin = board.GP19
led7_pin = board.GP28
led8_pin = board.GP27
led9_pin = board.GP26
led10_pin = board.GP22
led11_pin = board.GP21
led12_pin = board.GP20

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.UP

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.UP

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.UP

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.UP

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.UP

btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.UP

btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.UP

btn10 = digitalio.DigitalInOut(btn10_pin)
btn10.direction = digitalio.Direction.INPUT
btn10.pull = digitalio.Pull.UP

btn11 = digitalio.DigitalInOut(btn11_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.UP

btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.direction = digitalio.Direction.INPUT
btn12.pull = digitalio.Pull.UP

led1 = digitalio.DigitalInOut(led1_pin)
led1.direction = digitalio.Direction.OUTPUT
led1.value = False

led2 = digitalio.DigitalInOut(led2_pin)
led2.direction = digitalio.Direction.OUTPUT
led2.value = False

led3 = digitalio.DigitalInOut(led3_pin)
led3.direction = digitalio.Direction.OUTPUT
led3.value = False

led4 = digitalio.DigitalInOut(led4_pin)
led4.direction = digitalio.Direction.OUTPUT
led4.value = False

led5 = digitalio.DigitalInOut(led5_pin)
led5.direction = digitalio.Direction.OUTPUT
led5.value = False

led6 = digitalio.DigitalInOut(led6_pin)
led6.direction = digitalio.Direction.OUTPUT
led6.value = False

led7 = digitalio.DigitalInOut(led7_pin)
led7.direction = digitalio.Direction.OUTPUT
led7.value = False

led8 = digitalio.DigitalInOut(led8_pin)
led8.direction = digitalio.Direction.OUTPUT
led8.value = False

led9 = digitalio.DigitalInOut(led9_pin)
led9.direction = digitalio.Direction.OUTPUT
led9.value = False

led10 = digitalio.DigitalInOut(led10_pin)
led10.direction = digitalio.Direction.OUTPUT
led10.value = False

led11 = digitalio.DigitalInOut(led11_pin)
led11.direction = digitalio.Direction.OUTPUT
led11.value = False

led12 = digitalio.DigitalInOut(led12_pin)
led12.direction = digitalio.Direction.OUTPUT
led12.value = False

print("Inicio")

while True:
    if not btn1.value:
        print("Botón 1")
        led1.value = True
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
        led11.value = False
        led12.value = False
        #keyboard.press(Keycode.A)
        cc.send(ConsumerControlCode.MUTE)
        time.sleep(0.5)
        #keyboard.release(Keycode.A)
        
    if not btn2.value:
        print("Botón 2")
        led1.value = False
        led2.value = True
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
        led11.value = False
        led12.value = False
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.1)
        
    if not btn3.value:
        print("Botón 3")
        led1.value = False
        led2.value = False
        led3.value = True
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
        led11.value = False
        led12.value = False
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.1)
        
    if not btn4.value:
        print("Botón 4")
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = True
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
        led11.value = False
        led12.value = False
        layout.write("sudo nmap -p- -sS --min-rate 5000 --open -vvv -n -Pn -oG allPorts ")
        time.sleep(0.5)
        
    if not btn5.value:
        print("Botón 5")
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = True
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
        led11.value = False
        led12.value = False
        layout.write ("extractPorts allPorts\n")
        time.sleep(0.5)
        
    if not btn6.value:
        print("Botón 6")
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = True
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
        led11.value = False
        led12.value = False
        layout.write("sqlmap --tables --dbs --batch -u ")
        time.sleep(0.5)
        
    if not btn7.value:
        print("Botón 7")
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = True
        led8.value = False
        led9.value = False
        led10.value = False
        led11.value = False
        led12.value = False
        keyboard.press(Keycode.CONTROL, Keycode.C)
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.C)
                
    if not btn8.value:
        print("Botón 8")
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = True
        led9.value = False
        led10.value = False
        led11.value = False
        led12.value = False
        keyboard.press(Keycode.CONTROL, Keycode.V)
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.V)
        
    if not btn9.value:
        print("Botón 9")
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = True
        led10.value = False
        led11.value = False
        led12.value = False
        layout.write("Ah, eso no es chicharron de laucha,\n")
        layout.write("ni tampoco es moco de pavo!\n")        
        time.sleep(0.1)
        

    if not btn10.value:
        print("Botón 10")
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = True
        led11.value = False
        led12.value = False
        layout.write("Jajajjajajajajjajajajjaja\n")
        time.sleep(0.1)

    if not btn11.value:
        print("Botón 11")
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
        led11.value = True
        led12.value = False
        layout.write("https://www.instagram.com/endif_ok/\n")
        time.sleep(0.5)
        
    if not btn12.value:
        print("Botón 12")
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
        led11.value = False
        led12.value = True
        layout.write("https://otroblogdemarcelo.wordpress.com/\n")
        time.sleep(0.5)
    
    time.sleep(0.05)
