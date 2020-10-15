

a=int(input("A类水笔的规格："))
b=int(input("A类水笔的价格："))
c=int(input("B类水笔的规格："))
d=int(input("B类水笔的价格："))
A=b/a
B=d/c
if A>B:
    print("选择B类水笔")
else:
    print("选择A类水笔")
