# 최빈값 구하기
'''
Kor
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.
Eng
The mode is the value that appears most frequently in a given set of data. Complete the function solution that takes an integer array array as a parameter and returns the mode. If there is more than one mode, return -1.
'''

def solution(array):
    freq={}
    for num in array:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    maxfreq=max(freq.values())
    mode=[num for num, value in freq.items() if value==maxfreq]
    if len(mode) > 1:
        return -1
    else:
        return mode[0]

array=input("배열을 입력하세요: ")
array=list(map(int, array.split()))
print("최빈값은",solution(array),"입니다")