weight = int(input('Enter your weight: '))
unit = input("(L)lbs or (K)kg :")

if unit.upper() == 'L':
    converted_weight = weight * 0.45
    print(f'your is {converted_weight}kilo')

else:
    converted_weight = weight / 0.45
    print(f'your is {converted_weight}puonds')
