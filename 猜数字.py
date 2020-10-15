a=4

while(1):
    b=int(input("请输入你所猜的数字："))
    if a<b:
        print("太大")
    elif a>b:
        print("太小")
    elif a==b:
        print("恭喜！猜中")
        break
