# 특정한 문자를 대문자로 바꾸기
'''
Kor
영소문자로 이루어진 문자열 my_string과 영소문자 1글자로 이루어진 문자열 alp가 매개변수로 주어질 때, my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
Eng
Write a function named solution that takes two parameters: a string my_string made up of lowercase letters, and a single lowercase letter alp. The function should return a new string where all occurrences of alp in my_string are converted to uppercase.
'''
def solution(my_string, alp):
    answer = ''.join(char.upper() if char == alp else char for char in my_string)
    return answer

my_string=str(input("※ 문자열을 입력해주세요: "))
if my_string.islower() and my_string.isalpha():
    print("my_string이 입력되었습니다.")
else:
    print("my_string은 영소문자만 허용됩니다.")
    quit()
alp=input("※ 대문자로 바꿀 문자를 입력해주세요: ")
if alp.islower() and alp.isalpha():
    print("alp이 입력되었습니다.")
else:
    print("alp는 영소문자만 허용됩니다.")
    quit()
    
print(solution(my_string, alp))

'''
# 중요 개념

※ join()
여러 개의 작은 문자열을 하나의 큰 문자열로 합치는 데에 사용된다.
'문자열 사이에 무엇을 배치해서 합칠까?'에 대한 답 역시 주어져야 한다.
예를 들어 만약 문자열 사이에 스페이스바를 두고 싶다면
sentence=' '.join(words)
를 입력하는 식이다.

※ 리스트 컴프리헨션
리스트를 만들 때에 사용되는 짧고 간결한 방법이다.
해당 방법을 통해 반복문과 조건문을 한 줄에 써서 새로운 리스트를 만들 수 있다.
예를 들면
numbers = [1,2,3,4,5]
squares = [x*x for x in numbers if x>2]
print(squares)를 하면
9, 16, 25가 출력되는 식이다.
'''