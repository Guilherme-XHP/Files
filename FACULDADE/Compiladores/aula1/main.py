import random
import math

num = random.randrange(1,100)
conta = 2 * (num * num) + math.cos(num)
final = 2 * (conta * conta) + math.cos(conta)

print(final)
    