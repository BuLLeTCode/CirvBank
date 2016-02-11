'''
Seit doma likt visadas fukncijas kas neder citur
'''
def is_credit(T, account):
    if T.account_from == account:
        T.credit=False
    else:
         T.credit=True
    return T
