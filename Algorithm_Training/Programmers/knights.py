# 기사단원의 무기

'''
Kor
숫자나라 기사단의 각 기사에게는 1번부터 number까지 번호가 지정되어 있습니다. 기사들은 무기점에서 무기를 구매하려고 합니다.
각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매하려 합니다. 단, 이웃나라와의 협약에 의해 공격력의 제한수치를 정하고, 제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 기사는 협약기관에서 정한 공격력을 가지는 무기를 구매해야 합니다.
예를 들어, 15번으로 지정된 기사단원은 15의 약수가 1, 3, 5, 15로 4개 이므로, 공격력이 4인 무기를 구매합니다. 만약, 이웃나라와의 협약으로 정해진 공격력의 제한수치가 3이고 제한수치를 초과한 기사가 사용할 무기의 공격력이 2라면, 15번으로 지정된 기사단원은 무기점에서 공격력이 2인 무기를 구매합니다. 무기를 만들 때, 무기의 공격력 1당 1kg의 철이 필요합니다. 그래서 무기점에서 무기를 모두 만들기 위해 필요한 철의 무게를 미리 계산하려 합니다.
기사단원의 수를 나타내는 정수 number와 이웃나라와 협약으로 정해진 공격력의 제한수치를 나타내는 정수 limit와 제한수치를 초과한 기사가 사용할 무기의 공격력을 나타내는 정수 power가 주어졌을 때, 무기점의 주인이 무기를 모두 만들기 위해 필요한 철의 무게를 return 하는 solution 함수를 완성하시오.
Eng
In the land of Numberia, each knight from the knights' order is assigned a number from '1' to 'number'. The knights are looking to purchase weapons from the armory. Each knight wants to buy a weapon whose power corresponds to the number of divisors of their assigned number. However, due to an agreement with a neighboring country, there is a specified limit to the weapon power. Knights whose weapon power would exceed this limit must purchase weapons with a power defined by the regulatory agency.
For example, the knight assigned number 15 has divisors 1, 3, 5, and 15, totaling 4, so they would normally buy a weapon with a power of 4. However, if the agreement with the neighboring country sets the power limit at 3 and the regulated power for exceeding knights at 2, then the knight with number 15 would purchase a weapon with a power of 2 from the armory. The production of each weapon requires 1 kg of iron per unit of power. Therefore, the armory owner needs to calculate the total weight of iron required to manufacture all the weapons.
Write a function solution that takes the total number of knights number, the power limit set by the agreement limit, and the power power for knights exceeding this limit, and returns the total weight of iron needed to produce all the weapons.

# 제한사항 (Constraints)
1 ≤ number ≤ 100,000
2 ≤ limit ≤ 100
1 ≤ power ≤ limit
'''
import numpy as np

def solution(number, limit, power):
    answer=0
    for i in range(1,number+1):
        divisor_number=0
        for j in range(1,i+1):
            if i%j==0:
                divisor_number+=1
        if divisor_number > limit:
            answer += power
        else:
            answer += divisor_number
    return answer

number = int(input("※ 기사단원의 수를 입력해주세요: "))
if 1<=number and number<=100000:
    print("기사단원의 수가 입력되었습니다")
else:
    print("숫자는 1 이상이며 100,000 이하여야 합니다.")
    quit()

limit = int(input("※ 공격력의 제한수치를 입력해주세요: "))
if 2<=limit and limit<=100:
    print("제한수치가 입력되었습니다")
else:
    print("숫자는 2 이상이며 100 이하여야 합니다.")
    quit()
    
power = int(input("※ 제한수치를 초과한 기사가 사용할 무기의 공격력을 입력해주세요: "))
if 1<=power and power<=limit:
    print("초과 상황에서의 공격력이 입력되었습니다")
else:
    print("숫자는 1 이상이며 제한수치의 값 이하여야 합니다.")
    quit()

result=solution(number, limit, power)
print("무기를 만들기위해선",result,"kg의 철이 필요합니다.")

'''
# 올바른 정답 (Right Answer)

def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        divisor_count = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                if j == i // j:
                    divisor_count += 1  # 제곱수인 경우 (예: 4 * 4 = 16)
                else:
                    divisor_count += 2  # 제곱수가 아닌 경우 (예: 1 * 16 = 16, 2 * 8 = 16)
        if divisor_count > limit:
            answer += power  # 약수의 개수가 제한보다 많다면 power 사용
        else:
            answer += divisor_count  # 그렇지 않다면 약수의 개수만큼 철을 사용
    return answer

# 해설 (Explanation)

◎ 기본 개념: 약수(Divisor)
숫자 n의 약수는 n을 나누어 떨어뜨릴 수 있는 숫자들입니다. 예를 들어, 28의 약수는 1, 2, 4, 7, 14, 28입니다.

◎ 왜 제곱근까지만 검사할까?
숫자 n의 약수를 찾을 때, n을 그 제곱근보다 작거나 같은 수로 나눴을 때 나누어 떨어지면, 몫 역시 n의 약수입니다. 이는 약수가 쌍을 이룬다는 성질 때문입니다.

예를 들어, 28을 생각해 보면:
28 ÷ 1 = 28 → 약수는 1과 28
28 ÷ 2 = 14 → 약수는 2와 14
28 ÷ 4 = 7 → 약수는 4와 7
제곱근 이상의 수로 나누어볼 필요가 없는 이유는, 제곱근을 초과하는 수들로 나눌 경우 그 몫이 이미 제곱근 이하에서 나왔기 때문입니다. 따라서, n의 제곱근까지만 검사하면 모든 약수를 찾을 수 있습니다.

◎ 약수의 개수가 제한을 초과하는 경우의 처리
문제에서는 약수의 개수가 limit을 초과하면 특정 공격력 power를 사용하도록 합니다. 약수의 개수를 모두 세지 않고도 초과 여부만 판단할 수 있습니다. 제곱근까지의 검사 도중 약수의 개수가 limit보다 많이 세어지면 바로 power를 사용합니다.

'''