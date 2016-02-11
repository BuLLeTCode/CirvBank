from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import random
from django.utils import timezone

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    number = models.CharField(max_length=50, blank=True)
    balance = models.IntegerField(default=0)
    date_created = models.DateTimeField('date published', default=timezone.now)

    #save metodes overraids, lai varetu pievienot uzgenereto konta numuru
    def save( self, *args, **kw ):
        if self.pk is None:
            self.number = Account.generate_account_number()
        super(Account, self ).save( *args, **kw )

    #izveido konta numuru
    @staticmethod
    def generate_account_number():
        while True:
            first = random.randint(01, 99)
            second  = random.randint(111111111111, 999999999999)
            a_number = "LV%02dCIBA%u" % (first, second)
            result = Account.objects.filter(number=a_number)
            #ja datubaze tada nav, tad atgriez
            if len(result) == 0:
                break
        return a_number

class Transaction(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)
    pass
