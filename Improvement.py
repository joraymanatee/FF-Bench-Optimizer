user_bench = {}
print('Say STOP to end player addition.')
while True:
    user_input = input('List your current players seperated in this format: (FIRSTNAME, LASTNAME)')
    if user_input != 'STOP':
        user_bench[user_input] = ''
    else:
        break


print(user_bench)


