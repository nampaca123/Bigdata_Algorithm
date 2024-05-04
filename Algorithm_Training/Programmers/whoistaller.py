# 머쓱이보다 키 큰 사람
'''
Kor
머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요. 
Eng
Meossuk is curious about where he should stand when his class lines up in order of height at school. Given an array of integers array containing the heights of Meossuk's classmates and an integer height representing Meossuk's height, complete the solution function to return the number of people taller than Meossuk.
'''
def solution(array,height):
    result = 0
    for i in array:
        if i > height:
            result += 1
    return result
        
array=[158,160,171,183,186]
height=int(input("머쓱이의 키를 입력하세요: "))
print(solution(array,height),"명이 머쓱이보다 키가 큽니다.")