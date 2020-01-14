from django.db import models

# Create your models here.


class WM_Market(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=1000)
    DbName = models.CharField(max_length=1000)
    ConnectionString = models.CharField(max_length=1000)

    def _str_(self):
        return self.Name

    class Meta:
        verbose_name = 'WM_Market'


class WM_MarketPropertyDataElements(models.Model):
    PropertyID = models.IntegerField(primary_key=True)
    PropertyName = models.CharField(max_length=250)
    Description = models.CharField(max_length=750)

    class Meta:
        verbose_name = 'WM_MarketPropertyDataElements'


class WM_MarketPropertyData(models.Model):
    PropertyDataID = models.IntegerField(primary_key=True)
    PropertyID = models.IntegerField()
    PropertyValue = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'WM_MarketPropertyData'
