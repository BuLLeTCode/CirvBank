from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import random, decimal
from django.utils import timezone
from django.db.models import Q
from banking.utils import is_credit
#from django.core.validators import RegexValidator

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    number = models.CharField(max_length=50, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    #phone_regex = RegexValidator(regex=r'^/e/{9,15}$', message="Telefona numura formats: '+371 12345678'.")
    phone_number = models.CharField(max_length=12, blank=True,
                                    help_text="Formats, piemeram, +31721241275") #Telefona numurs ar visu REGEX! :)

    #List ar Choices, cerams, pietiks ar diviem dzimumiem :)
    DZIMUMS = (
        ('S', 'Sieviete'),
        ('V', 'Virietis'),
    )
    gender = models.CharField(max_length=1, choices=DZIMUMS, blank=True)
    birth_date = models.DateField(default=timezone.now)
    city = models.CharField(max_length=20, blank=True,
                            help_text="Piemeram, Riga")
    address = models.CharField(max_length=50, blank=True,
                               help_text="Piemeram, Liela iela 15a")
    Postcode = models.CharField(max_length=10, blank=True,
                                help_text="Piemeram, LV-4512")
    contacting_password = models.CharField(max_length=50, blank=True,
                                           help_text="Parole, kas tiek izmantota sazinai ar banku")

    date_created = models.DateTimeField('Izveidosanas datums', default=timezone.now)

    #visi parskaitijumi kuros konts piedalijies
    def transactions(self, count = None):
        if count:
            t = Transaction.objects.filter(Q (account_from=self) | Q(account_to=self) ).order_by('-date_created')[:count]
            #apskata visus elementus un iestata lauku 'credit' ja naudu sanem lietotajs, kas skatas lapu
            return map(lambda tr: is_credit(tr, self), t)
        else:
            t = Transaction.objects.filter(Q (account_from=self) | Q(account_to=self) ).order_by('-date_created')[:count]
            return map(lambda tr: is_credit(tr, self), t)

    #nosaukuma  konta numurs un vards, uzvards
    def __str__(self):
        return "%s %s : %s" % (self.user.first_name, self.user.last_name, self.number)

    #save metodes overraids, lai varetu pievienot uzgenereto konta numuru
    def save(self, *args, **kw ):
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
    account_from = models.ForeignKey(Account, related_name='account_from', on_delete=models.CASCADE)
    account_to = models.ForeignKey(Account, related_name='account_to', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_created = models.DateTimeField('Parskaitijuma datums', default=timezone.now)

    # parskaitissanas metode. jaizsauc skataa (views.py)
    def transfer(self):
        # parbauda vai pietiek naudas
        if not self.account_from.balance > self.amount:
            return False

        self.account_from.balance -= decimal.Decimal(self.amount)
        self.account_from.save()
        self.account_to.balance += decimal.Decimal(self.amount)
        self.account_to.save()

        return True
