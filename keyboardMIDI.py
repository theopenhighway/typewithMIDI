import rtmidi
import pyautogui
from time import sleep
#pyautogui.PAUSE = 2.5

intr = rtmidi.MidiIn()
ports = intr.get_ports()
# print(ports)
intr.open_port(1)

def MIDItoText(noteNum, velocity):
    match noteNum:
        case 20:
            pyautogui.press('space')
        case 21:
            pyautogui.press('backspace')
        case 22:
            pyautogui.press('enter')
        case 48:
            letter = 'a'
            fontCase(velocity, letter)
        case 49:
            letter = 'b'
            fontCase(velocity, letter)
        case 50: 
            letter = 'c'
            fontCase(velocity, letter)
        case 51:
            letter = 'd'
            fontCase(velocity, letter)
        case 52:
            letter = 'e'
            fontCase(velocity, letter)
        case 53:
            letter = 'f'
            fontCase(velocity, letter)
        case 54:
            letter = 'g'
            fontCase(velocity, letter)
        case 55:
            letter = 'h'
            fontCase(velocity, letter)
        case 56:
            letter = 'i'
            fontCase(velocity, letter)
        case 57:
            letter = 'j'
            fontCase(velocity, letter)
        case 58:
            letter = 'k'
            fontCase(velocity, letter)
        case 59:
            letter = 'l'
            fontCase(velocity, letter)
        case 60:
            letter = 'm'
            fontCase(velocity, letter)
        case 61:
            letter = 'n'
            fontCase(velocity, letter)
        case 62:
            letter = 'o'
            fontCase(velocity, letter)
        case 63:
            letter = 'p'
            fontCase(velocity, letter)
        case 64:
            letter = 'q'
            fontCase(velocity, letter)  
        case 65:
            letter = 'r'
            fontCase(velocity, letter)
        case 66:
            letter = 's'
            fontCase(velocity, letter)
        case 67:
            letter = 't'
            fontCase(velocity, letter)
        case 68:
            letter = 'u'
            fontCase(velocity, letter)
        case 69:
            letter = 'v'
            fontCase(velocity, letter) 
        case 70:
            letter = 'w'
            fontCase(velocity, letter)
        case 71:
            letter = 'x'
            fontCase(velocity, letter)
        case 72:
            letter = 'y'
            fontCase(velocity, letter)
        case 73:
            letter = 'z'
            fontCase(velocity, letter)
        case 74:
            pyautogui.write('0')
        case 75:
            pyautogui.write('1')
        case 76:
            pyautogui.write('2')
        case 77:
            pyautogui.write('3')
        case 78:
            pyautogui.write('4')
        case 79:
            pyautogui.write('5')
        case 80:
            pyautogui.write('6')
        case 81:
            pyautogui.write('7')
        case 82:
            pyautogui.write('8')
        case 83:
            pyautogui.write('9')

def fontCase(velocity,letter):
    if velocity < 101:
        pyautogui.write(letter.lower())
    elif velocity > 100 :
        pyautogui.write(letter.upper())

while True:
    msgde = intr.get_message()

    if msgde:
        (msg, dt) = msgde
        command = hex(msg[0])
        notestat = msg[0]
        notes = msg[1]
        velocity = msg[2]
        
        # get motor ref numbergpio 
        if command == '0x90':
            MIDItoText(notes, velocity)
            print(f"{command} {msg[1:]}\t| dt = {dt:.2f}")
    else: 
        sleep(0.001)
       