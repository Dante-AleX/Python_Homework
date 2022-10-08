# Вычислить число c заданной точностью d

def input_numbers():

    while True:
        num = input('Insert a number: ')
        try:
            number = float(num)
            return number
        except:
            print("You didn't insert a number. Try again.")

def input_count():
    while True:
        num = input('Insert a precise number for rounding: ')
        try:
            numbers = int(num)
            return numbers
        except:
            print("You didn't insert a number. Try again.")

number = input_numbers()
count = input_count()

print(f'{number:.{count}f}')
