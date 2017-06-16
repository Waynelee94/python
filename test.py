def Menu():
    print('======================================')
    print('''(1)caculate the sum of five numbers''')
    print('''(2)caculate the average of five numbers''')
    print('''(X)exit''')

def Sum():
    list = [1,2,3,4,5]
    i = 0
    sum = 0
    while i < len(list):
        list[i] = float(input('Please input the %dth number:' %(i + 1)))
        sum = sum + list[i]
        i += 1
    return sum

def Aver():
    sum = Sum()
    aver = float(sum / 5)
    return aver

while True:
    Menu()
    option = str(input('Please choose an option:'))
    if option == '1':
        result = Sum()
        print(result)
        continue
    elif option == '2':
        result = Aver()
        print(result)
        continue
    elif option == 'X':
        print('system exit')
        break
    else:
        print('wrong option')
        continue
