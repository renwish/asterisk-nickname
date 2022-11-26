a = 0
b = 4

for row in range(5):
    for col in range(20):
        if col in [0,8,15,19]:
            print('*', end = '')
        elif row == 0 and col in [1,2,3,9,10,11,12]:
            print('*', end = '')
        elif row == 1 and col in [4,16]:
            print('*', end = '')
        elif row == 2 and col in [1,2,3,9,10,17]:
            print('*', end = '')
        elif row == 3 and col in [4,18]:
            print('*', end = '')
        elif row == 4 and col in [5,9,10,11,12]:
            print('*', end = '')
        else:
            print(end=' ')
    print()
