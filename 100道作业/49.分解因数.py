def fun(a, t=2):
     count = 0
     if a <t:
         return count
     else:
         for i in range(t, int(a / 2) + 1):
             if a % i == 0:
                temp = a // i
                 if temp >= i: 
                     count += 1
                     count += fun(temp, i)
         return count


num = int(input())
print(fun(num) + 1)
