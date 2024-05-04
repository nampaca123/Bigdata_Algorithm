# a와 b 출력하기
'''
Kor
정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.
Eng
Given integers a and b, write a code that takes these numbers as input and outputs them in the format shown in the examples.
'''

a, b = map(int, input("a와 b의 값을 입력하세요: ").split(' '))
print("a =",a)
print("b =",b)

'''
map() 함수는 객체값과 객체를 전달받아 새로운 형태로 변환해서 사용할 수 있다.
위의 함수에서는 input()을 입력받은 다음,
split()으로 공백을 기준으로 입력받은 '4 5' 등의 값을 [4, 5]로 분리한 뒤
int값으로 변환하여 각각의 a와 b에게 전달하는 식이다.
'''