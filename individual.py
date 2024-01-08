


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
dif = num1 - num2
mult = num1 * num2

if num2 != 0:
    div = num1 / num2
else:
    div = "Divission not possible"

print(f"Сумма: {sum}")
print(f"Разность: {dif}")
print(f"Произведение: {mult}")
print(f"Частное: {div}")