from django.db import models


# Create your models here.

class Parent(models.Model):
    PARENT_BRAND = models.CharField(max_length=20)

    def __str__(self):
        return self.PARENT_BRAND


class Brand(models.Model):
    PARENT_BRAND = models.ForeignKey(Parent, on_delete=models.CASCADE, max_length=50)
    BRAND_NAME = models.CharField(max_length=30)

    SHAREHOLDER = models.BooleanField(default=False)
    SUBSIDIARY = models.BooleanField(default=False)
    SUB_BRAND = models.BooleanField(default=False)


    def setShareTrue(self):
        self.SHAREHOLDER = True
        self.save(update_fields=['SHAREHOLDER'])

    def setSubsidiaryTrue(self):
        self.SUBSIDIARY = True
        self.save(update_fields=['SUBSIDIARY'])

    def setSubBrandTrue(self):
        self.SUB_BRAND = True
        self.save(update_fields=['SUB_BRAND'])

    def __str__(self):
        return self.BRAND_NAME

