'''
Seit doma likt visadas fukncijas kas neder citur
'''
def is_credit(T, account):
    if T.account_from == account:
        T.credit=False
    else:
         T.credit=True
    return T

# naudu no centiem uz eiro parveido
def decimalize(ones):
    hundreds = float(ones) / 100
    return hundreds