# 素因数分解のアルゴリズム
import math

n = input("Enter the number: ")
n = int(n)

result = []
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        result.append(i)
        result.append(n // i) # 「//」は商を整数で返す除算

result.sort()

print(result)
