# RSA公開鍵暗号の暗号化と復号化の手順

# 素数pとqの選択
p=3
q=7

# nの計算
n=p*q

# 暗号化するメッセージの受け取り
m = input(f"Enter the number you want to encrypt (mest be less than {n}).: ")
m=int(m)
if m >= n:
    raise Exception("your input must be less than n")

# eとdの決定
k=5
# k*(p-1)*(q-1)+1=61
e=1
d=61

# 暗号化
c=pow(m,e)%n

# 復号化（入力値と同じであることを確認）
print(pow(c,d)%n)
