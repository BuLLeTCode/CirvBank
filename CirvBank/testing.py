import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CirvBank.settings")
import django
django.setup()
from banking.models import Account, Transaction


def get_some_account(id):
    return Account.objects.filter()[id]

def create_transaction():
    a1 = get_some_account(0)
    a2 = get_some_account(1)
    t = Transaction()
    t.account_from = a2
    t.account_to = a1
    t.amount = 2.50
    print("sender balance before %s" % a2.balance)
    print("receiver balance before %s" % a1.balance)
    print t.transfer()
    print("sender balance after %s" % a2.balance)
    print("receiver balance after %s" % a1.balance)
    t.save()

def get_some_transaction(id):
    return Transaction.objects.filter()[id]

a = get_some_account(0)
b = get_some_account(1)

def is_credit(T, account):
    if T.account_from == account:
        T.credit=False
    else:
         T.credit=True
    return T

col = map(lambda tr: is_credit(tr, b), b.transactions())
for c in col:
    print c.credit
print b
