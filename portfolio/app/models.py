from django.db import models

# Create your models here.

class Personal_Info(models.Model):
    name = models.CharField(max_length=200)
    Job_role= models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    phone_number= models.IntegerField()
    email_address = models.EmailField()
    reusme_link =models.URLField(default='not_available')
    linkedin = models.URLField(default='https://github.com/MONAlIS-A') 
    facebook_link =models.URLField(default='https://github.com/MONAlIS-A') 
    instagram_link= models.URLField(default='https://github.com/MONAlIS-A') 
    discord_link =models.URLField(default='https://github.com/MONAlIS-A') 


    
class Projects_list(models.Model):
    Name= models.CharField(max_length=200)
    Description =models.TextField()
    project_link = models.URLField()
    project_image =models.ImageField(upload_to="my_projects")
    github_link = models.URLField(default='not_available')
    vedio_link = models.URLField(default='not available')
   

    


    
