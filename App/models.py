from django.db import models

# Create your models here.
class profile(models.Model):
     Religion = (
          
               ('Muslim','Muslim'),
               ('Hindu','Hindu'),
               ('christian','christian'),
               ('Buddha','Buddha'),

          
     )
     name=models.CharField(max_length=50,null=True,blank=True)
     image=models.ImageField(upload_to='profile_pic/',default='default/def.jpg',null=True,blank=True)
     email=models.EmailField(max_length=20,null=True,blank=True)
     age=models.PositiveIntegerField(null=True,blank=True)
     address=models.TextField(max_length=50,null=True,blank=True)
     phone_no=models.TextField(max_length=50,null=True,blank=True)
     date_of_birth=models.TextField(max_length=50,null=True,blank=True)
     religion=models.CharField(max_length=9,choices=Religion)
     def __str__(self):
        return self.name