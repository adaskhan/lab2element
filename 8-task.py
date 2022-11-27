amount = 0


def add_to_bank_account(summa):
    global amount
    amount += summa
    print(f'${summa} added. You have ${amount}')


def subtract_from_bank_account(summa):
    global amount
    amount -= summa
    print(f'${summa} subtracted. You have ${amount}')


def money_conversion(summa, *cur):
    if cur[0].upper() == 'USD' and cur[1].upper() == 'KZT':
        return f'{summa * 465} {cur[1].upper()}'
    elif cur[1].upper() == 'USD' and cur[0].upper() == 'KZT':
        return f'{summa / 465} {cur[1].upper()}'


add_to_bank_account(500)
subtract_from_bank_account(200)
print(money_conversion(300, 'usd', 'KZT'))
print(money_conversion(139500, 'KZT', 'usd'))
