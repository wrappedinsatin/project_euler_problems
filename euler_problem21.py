from sympy import divisors

amicables = {}
amicable_sum = 0

for number in range(1,10001):
    amicables[number] = sum(divisors(number,proper=True))

for pair1 in amicables:
    pair2 = amicables.get(pair1)
    check = amicables.get(pair2)

    if check==pair1 and pair1!=pair2:
        amicable_sum += pair1 + pair2

amicable_sum /= 2
print(amicable_sum) #SOLVED: 31626