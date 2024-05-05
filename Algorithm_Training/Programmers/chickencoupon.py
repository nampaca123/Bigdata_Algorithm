# 치킨 쿠폰
'''
Kor
프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다. 시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.
Eng
Programmers Chicken issues one coupon for each chicken ordered. Once you collect ten coupons, you can get a chicken for free, and you also receive a coupon for this free chicken. Write a function 'solution' that returns the maximum number of free chickens you can receive, given the number of chickens 'chicken' that were ordered as a parameter.
'''
def solution(chicken):
    couponcount=0
    service=0
    while chicken>0:
        couponcount+=1
        chicken-=1
        if couponcount==10:
            couponcount=0
            chicken+=1
            service+=1
    return service   
    
chicken = int(input("치킨을 얼마나 주문했는지 입력하세요: "))
print("받을 수 있는 최대 서비스 치킨의 수는",solution(chicken),"개입니다.")

'''
for문은 사전에 정해둔 범위에서만 작동하며, 루프가 실행되는 중 그 범위를 수정하는 것이 불가능하다
반면 while문은 주어진 조건이 참인 동안 계속 작동하므로, 동적인 제어가 가능하다
'''