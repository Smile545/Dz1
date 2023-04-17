chislo1 = int(input())
chislo2 = int(input())
sum = chislo1 + chislo2
proiz = chislo1 * chislo2
print(sum)
print(proiz)
chislo2 = int((sum + ((-sum) ** 2 - 4 * proiz) ** 0.5) / 2)
chislo1 = int((sum - ((-sum) ** 2 - 4 * proiz) ** 0.5) / 2)
print(chislo1, chislo2)