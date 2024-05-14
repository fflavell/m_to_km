miles = 1
m_km = 1.61

answer = input('Type 1 to convert kilometres to miles or type 2 to convert miles to kilometres. \n')

while True:
    if answer == ('1'):
        print('Enter the number of kilometres you would like to convert to miles: ')
        km = int(input())
        print (km, 'kilometres is ', (km * 0.621371), ('in miles!'))
    elif answer == ('2'):
        print('Enter the number of miles you would like to convert to kilometres: ')
        m = int(input())
        print(m, 'miles is ', (m * 1.6), ('in kilometres!'))

    print('\nPress q to end program. Press p to run it again.')
    answer1 = input()
    if answer1 == ('p'):
            continue
    elif answer1 != ('q' or 'p'):
        print('Try again!')
    else:
        return
        

