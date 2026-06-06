
string = ""
number = 1

while len(string) <= 1000000:
    string += str(number)
    number += 1

champ_value = 1
n = 1

while n <= 1000000:
    champ_value *= int(string[n-1])
    n *= 10

print(champ_value) # SOLVED: 210