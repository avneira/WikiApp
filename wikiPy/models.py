from django.db import models

# Create your models here.
class theme(models.Model):
    nameTheme = models.CharField(max_length=128, null=True, blank=True)
    descriptionTheme = models.CharField(max_length=512, null=True, blank=True)

class article(models.Model):
    nameArticle=models.CharField(max_length=128, null=True, blank=True)
    contentArticle= models.CharField(max_length=1024, null=True, blank=True)
    themeR = models.ForeignKey(theme, null=True, blank=True, on_delete=models.SET_NULL)
    