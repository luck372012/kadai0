name=["たんじろう","ぎゆう","ねずこ","むざん"]
name.append("ぜんいつ")
print(name)

for i in name:
    print( i )

def check(n):
    for _ in name:
        if _ == n:
            print(f"{n}は含まれます")
            return
    print(f"{n}は含まれません")

check("たんじろう")
check("ねこ")
