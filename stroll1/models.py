from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300) 
    price = models.FloatField()
    img = models.ImageField(upload_to="pics")

    def __str__(self):
        return self.name
    
    @property 
    def imageUrl(self):
        try:
            url = self.img.url
        
        except:
            url = ''
        return url
    

class Custom(models.Model):
    name = models.CharField(max_length=100,null=True)
    destnation = models.CharField(max_length=100,null=True)
    activity = models.CharField(max_length=100, null=True)
    duration = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=100, null=True)

    # def __str__(self):
    #     return self.name

class Blogs(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=5000,null=True)
    price = models.CharField(max_length=100, null=True)
    img = models.ImageField(upload_to="pics")
    iframe = models.CharField(max_length=500, null=True)
    tag = models.CharField(max_length=500, null=True, blank=True)

    @property 
    def ImageUrl(self):
        try:
            url = self.img.url

        except:
            url = ''
            
        return url

    def __str__(self):
        return self.name