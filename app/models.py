from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(default='LogoDefault.png')
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Advocate(models.Model):

    name = models.CharField(max_length=50)
    profile_pic = models.ImageField(default='default_pic.jpg')
    short_bio = models.TextField(null=True, blank=True)
    long_bio = models.TextField(null=True, blank=True)
    advocate_since = models.DateField()
    company = models.ForeignKey(Company,related_name='advocates',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AdvocateLink(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField(max_length=100)
    advocate = models.ForeignKey(Advocate,related_name='links',on_delete=models.CASCADE)

    def __str__(self):
        return self.advocate.name + '-' +self.name

class CompanyLink(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField(max_length=100)
    company = models.ForeignKey(Company,related_name='links',on_delete=models.CASCADE)

    def __str__(self):
        return self.company.name + '-' +self.name