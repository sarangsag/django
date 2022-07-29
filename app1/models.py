import datetime

from django.db import models


# Create your models here.
class usmodel(models.Model):
    uname=models.CharField(max_length=20)
    uage=models.IntegerField()
    uphone=models.CharField(max_length=50)
    umail=models.EmailField(max_length=50)
    upsw=models.CharField(max_length=8)

    # def __str__(self):
    #     return self.umail


class add_pro(models.Model):
    # pid=models.CharField(max_length=100)
    pcompany=models.CharField(max_length=100)
    pname = models.CharField(max_length=100)
    file=models.ImageField()
    pram = models.CharField(max_length=100)
    prom = models.CharField(max_length=100)
    pcolor = models.CharField(max_length=100)
    pprice = models.IntegerField()
    pitems=models.IntegerField()


class feedbackmodel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    sub=models.CharField(max_length=100)
    mes=models.CharField(max_length=100)
    dt=models.DateTimeField()

#
class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    BOOK_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    pname = models.CharField(max_length=50)
    dmail=models.EmailField(max_length=50)
    pprice = models.CharField(max_length=50)
    pcolor = models.CharField(max_length=50)
    pram = models.CharField(max_length=50)
    prom = models.CharField(max_length=50)
    quantity=models.IntegerField()
    name=models.CharField(max_length=20)
    number=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    dt=models.DateTimeField()
    lmark=models.CharField(max_length=50)
    dtype=models.CharField(max_length=20)
    file=models.ImageField()
    payment=models.CharField(max_length=50)
    pid = models.CharField(max_length=100)
    total=models.IntegerField()
    status = models.CharField(choices=BOOK_STATUSES, default=BOOKED, max_length=20)



class cart(models.Model):
        pname = models.CharField(max_length=100)
        file = models.ImageField()
        pram = models.CharField(max_length=100)
        prom = models.CharField(max_length=100)
        pcolor = models.CharField(max_length=100)
        pprice = models.IntegerField()
        us=models.EmailField(max_length=50)
        # total=models.IntegerField()
