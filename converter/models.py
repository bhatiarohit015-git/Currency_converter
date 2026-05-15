from django.db import models

# Create your models here.
class  Currency_converter(models.Model):
    amount= models.FloatField(blank=True,null=True)
    converted_amount=models.FloatField(blank=True,null=True)
    select_currency=models.CharField(blank=True,null=True)
    converted_currency=models.CharField(blank=True,null=True)
    class Meta:
        # verbose_name = _("")
        # verbose_name_plural = _("s")

     def __str__(self):
        return self.id