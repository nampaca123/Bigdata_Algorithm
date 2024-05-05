# 겹치는 선분의 길이
'''
Kor
선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.
Eng
Three line segments are laid out in parallel. The starting and ending coordinates of each line segment are provided in a 2D array lines in the format [[start, end], [start, end], [start, end]]. Write a function 'solution' that returns the length of the section where two or more line segments overlap, given the parameter lines.
'''
# work on progress
def solution(lines):
    lines.sort(key=lambda x: x[0])
    overlapping=0
    currentend=lines[0][1]
    
    for start, end in lines[1:]:
        if currentend > start:
            overlapping+=min(currentend,end)-start
        currentend=max(currentend,end)
    return overlapping

lines=[]
for i in range(3):
    makingline=input(f"{i}번 선분의 시작과 끝을 입력하세요: ")
    eachline=list(map(int,makingline.split()))
    lines.append(eachline)