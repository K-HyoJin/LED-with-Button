from pyfirmata import Arduino,util
import time

#핀 모드 세팅
board = Arduino('COM8')

digital_input = board.get_pin('d:2:i') # 2번 핀 입력으로 설정
led = board.get_pin('d:13:o') #8번 핀 출력으로 설정

it = util.Iterator(board) #회로의 입력상태를 읽어올 변수선언
it.start()

while True:
    switch = digital_input.read()
    if switch is True:
        led.write(1)
    else:
        led.write(0)
    time.sleep(0.1)
