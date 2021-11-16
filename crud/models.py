from django.db import models
from django.forms import ModelForm

class Person(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.fname + ' ' + self.lname

class PersonModelForm(ModelForm):
    class Meta:
        model = Person
        exclude = ['id']