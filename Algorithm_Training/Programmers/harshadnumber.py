# 하샤드 수
'''
Kor
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
Eng
An integer x is a Harshad number if it is divisible by the sum of its digits. For example, the sum of the digits of 18 is 1+8=9, and since 18 is divisible by 9, 18 is a Harshad number. Write a function, 'solution/, that takes a natural number x as input and checks whether x is a Harshad number
'''
def solution(x):
    num = [int(i) for i in str(x)]
    sumnum = sum(num)
    answer = (x%sumnum==0)
    return answer
x = int(input("하샤드 수를 입력하세요: "))
print(solution(x))

'''
int에 str을 덧씌울 시에 각각의 자릿수가 별개의 문자로 할당된 문자열로 변환된다
'''