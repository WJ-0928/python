while(1):
    a=int(input("请输入成绩："))
    if a>=0 and a<=100:
        if a<60:
            print("成绩等级为：E")
        elif a>=60 and a<=69:
            print("成绩等级为：D")
        elif a>=70 and a<=79:
            print("成绩等级为：C")
        elif a>=80 and a<=89:
            print("成绩等级为：B")
        elif a>=90:
            print("成绩等级为：A")

    else:
        print("输入错误")
        break

