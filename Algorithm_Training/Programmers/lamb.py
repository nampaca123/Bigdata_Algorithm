# 양꼬치
'''
Kor
머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 정수 n과 k가 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.
Eng
At the Meossuk's skewer restaurant, customers receive one free drink for every 10 skewer portions they purchase. Each skewer portion costs 12,000 won, and each drink is priced at 2,000 won. Given integers n and k as parameters, complete the solution function that returns the total amount due for consuming n skewer portions and k drinks.
'''
def solution(n,k):
    price=0
    price+=12000*n
    price+=2000*(k-int(n/10))
    return price

n=int(input("먹은 양꼬치의 수를 입력하세요: "))
k=int(input("마신 음료수의 수를 입력하세요: "))
print(solution(n,k),"원입니다")