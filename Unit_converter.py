print('Hello this program converts kilometers into miles!!')

while True:
    kilometers = float(input("Please enter a number of kilometers that you'd like to convert into miles. Enter only a number: ").replace(',', '.'))
    miles = kilometers * 0.621371192
    print(f'{kilometers} kilometers is equal to {miles} miles')
    another_conversion = input('Would you like another conversion(y/n)? ').lower()
    if another_conversion == 'y':
        pass
    else:
        print('Have a good day!!')
        break