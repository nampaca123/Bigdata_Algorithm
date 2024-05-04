# 과일 장수
'''
Kor
과일 장수가 사과 상자를 포장하고 있습니다. 사과는 상태에 따라 1점부터 k점까지의 점수로 분류하며, k점이 최상품의 사과이고 1점이 최하품의 사과입니다. 사과 한 상자의 가격은 다음과 같이 결정됩니다.
한 상자에 사과를 m개씩 담아 포장합니다.
상자에 담긴 사과 중 가장 낮은 점수가 p (1 ≤ p ≤ k)점인 경우, 사과 한 상자의 가격은 p * m 입니다.
과일 장수가 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익을 계산하고자 합니다.(사과는 상자 단위로만 판매하며, 남는 사과는 버립니다)
예를 들어, k = 3, m = 4, 사과 7개의 점수가 [1, 2, 3, 1, 2, 3, 1]이라면, 다음과 같이 [2, 3, 2, 3]으로 구성된 사과 상자 1개를 만들어 판매하여 최대 이익을 얻을 수 있습니다.
(최저 사과 점수) x (한 상자에 담긴 사과 개수) x (상자의 개수) = 2 x 4 x 1 = 8
사과의 최대 점수 k, 한 상자에 들어가는 사과의 수 m, 사과들의 점수 score가 주어졌을 때, 과일 장수가 얻을 수 있는 최대 이익을 return하는 solution 함수를 완성해주세요.
Eng
A fruit vendor is packing apples into boxes. The apples are graded on a scale from 1 to k, where k points represent the highest quality and 1 point the lowest. The price of a box of apples is determined as follows:
Each box is packed with m apples.
If the lowest score among the apples in a box is p (1 ≤ p ≤ k), then the price of the box is p * m.
The vendor wants to maximize their earnings by selling as many apples as possible (apples are only sold by the box, and any leftovers are discarded).
For example, if k = 3, m = 4, and there are 7 apples with scores [1, 2, 3, 1, 2, 3, 1], the vendor can pack a single box with apples [2, 3, 2, 3] to achieve the maximum profit:
(Lowest apple score in the box) x (Number of apples per box) x (Number of boxes) = 2 x 4 x 1 = 8
Given the maximum apple score k, the number of apples per box m, and the scores of the apples score, write a function solution that returns the maximum profit the vendor can achieve.
'''
# work on progress

def solution(k,m,score):
    maxprofit=0
    score.sort()
    
    for i in range(len(score)-m+1):
        box=score[i:i+m]
        minnum=min(box)
        boxprofit=minnum*m
        maxprofit=max(maxprofit,boxprofit)
    return maxprofit
        
    
k = int(input("※ 사과의 최대 점수를 입력해주세요: "))
if 3<=k and k<=9:
    print("사과의 최대 점수가 입력되었습니다")
else:
    print("숫자는 3 이상이며 9 이하여야 합니다.")
    quit()

m = int(input("※ 한 상자에 들어가는 사과의 수를 입력해주세요: "))
if 3<=m and m<=10:
    print("상자 속 사과의 수가 입력되었습니다")
else:
    print("숫자는 3 이상이며 10 이하여야 합니다.")
    quit()
    
score = input("※ 사과들의 점수를 입력해주세요: ")
score = list(map(int, score.split()))
if 7<=len(score) and len(score)<=1000000:
    print("사과들의 점수가 입력되었습니다")
else:
    print("길이는 7 이상이며 1000000 이하여야 합니다.")
    quit()
print(solution(k,m,score))