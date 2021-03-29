num = input('Enter a number or an alphabet to exit')

lst_num = list()
while(num.isnumeric()):
    lst_num.append(float(num))
    num = input('Enter another number or alphabet to exit')
else:
    print(f'The largest number of  all the input data is {max(lst_num)} ')
    print(f'The least number of all the input data is {min(lst_num)} ')
    print(f'The sum of all the input data is {sum(lst_num)}')
    print('Thank you for using the program')
            