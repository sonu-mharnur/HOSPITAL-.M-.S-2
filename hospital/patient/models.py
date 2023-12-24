from django.db import models


# Create your models here.
class hospitaldata(models.Model):
    hospitaldata_name = models.CharField('hospital_name',max_length=100)
    hospitaldata_contact = models.IntegerField('hospital_contact',max_length=12)
    hospitaldata_address = models.TextField('hospital_address')
    hospitaldata_email = models.EmailField()
    hospitaldata_specilazation = models.CharField('hospital_specialization',max_length=200)

    def __str__(self):
        return self.hospitaldata_name