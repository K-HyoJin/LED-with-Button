# Arduino example 2 
Tutorial 2 - LED with Button \
버튼을 누르면 LED가 켜지고 버튼을 누르지 않을 때는 LED가 꺼지게 동작하도록 제작


## circuit
LED -> digital 13pin \
![image](https://user-images.githubusercontent.com/79436159/108667697-1ca4dd00-751d-11eb-90b3-79945ec1a951.png)


## code
``` from pyfirmata import Arduino,util ```\
pyfirmata의 아두이노 모듈을 사용하기 위해 import함 

``` board = Arduino('COM8')``` \
변수1 = Arduino('**포트번호**') 를 해서 보드와 연결 

``` digital_input = board.get_pin('d:2:i')``` \
  -> 2번핀을 digital신호 입력핀으로 설정\
변수1 = 변수2.get_pin('**d or a** : **pin number** : **i or o** ') \
**d or a** : The type of the pin \
**pin number** : The number of the pin\
**i or o** : The mode of the pin 
 
 ``` it = util.Iterator(board) ```\
보드의 입력값을 지속적으로 업데이트해주는 iterator 변수 선언

 ``` it.start()``` \
iterator 시작

``` switch = digital_input.read()```\
button과 연결된 2번핀의 입력을 읽어와서 변수 switch에 저장

```led.write(1)```\
led가 연결된 13번 핀에 1을 주어 led를 켜도록 함

```  time.sleep(0.1) ```\
0.1초동안 기다림

