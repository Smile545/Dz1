n = int(input("Введите число N "))
a = 2
s = 0
while a < n:
    a = a ** s
    s = s + 1
    if a < n:
        print(a)
        a = 2
    else:
        break
