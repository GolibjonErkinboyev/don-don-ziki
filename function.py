name1 = str(input("Birinchi o'yinchi ismingizni kiriting: "))
name2 = str(input("Ikkinchi o'yinchi ismingizni kiriting: "))
print("O'yin boshlandi:")
def  shart():
    print("Qaychi -> 1\n Qog'oz -> 2\n Tosh -> 3")
shart()
num1 = int(input(f'{name1} shart boyicha raqamni kiriting: '))
num2 = int(input(f'{name2} shart boyicha raqamni kiriting: '))
if num1 == 1 and num2 == 2:
    print(f'Qaychi qogozni yutadi {name1} g`olib bo`ldi!')
elif num1 == 1 and num2 == 3:
    print(f'Tosh qaychini yutadi {name2} g`olib bo`ldi!')
elif num1 == 2 and num2 == 1:
    print(f'Qaychi qogozni yutadi {name2} g`olib bo`ldi!')
elif num1 == 2 and num2 == 3:
    print(f'Tosh qaychini yutadi {name1} g`olib bo`ldi!')
elif num1 == 3 and num2 == 1:
    print(f'Tosh qaychini yutadi {name1} g`olib bo`ldi!')
elif num1 == 3 and num2 == 2:
    print(f'Qog`oz toshni yutadi {name2} g`olib bo`ladi!')
else:
    print("Natija DURRANG!")