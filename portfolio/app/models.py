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
    github_link = models.URLField(default='https://github.com/')
    discord_link =models.URLField(default='https://github.com/MONAlIS-A') 


    
class Projects_list(models.Model):
    CATEGORY_CHOICES = [
        ('Backend', 'Backend Projects'),
        ('Data Engineering', 'Data Engineering Projects'),
        ('Data Analysis', 'Data Analysis Projects'),
        ('AI & Machine Learning', 'AI & Machine Learning Projects'),
    ]
    Name= models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Backend')
    Description =models.TextField()
    project_link = models.URLField()
    project_image =models.ImageField(upload_to="my_projects")
    github_link = models.URLField(default='not_available')
    vedio_link = models.URLField(default='not available')

    def __str__(self):
        return self.Name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Backend', 'Backend Development'),
        ('Data Engineering', 'Data Engineering'),
        ('Data Analysis', 'Data Analysis'),
        ('AI', 'Data Science & AI'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    icon_url = models.URLField(blank=True, null=True, help_text="URL for the skill icon/logo")
    details = models.TextField(help_text="Comma-separated focus areas or details")

    def __str__(self):
        return f"{self.name} ({self.category})"

    def get_details_list(self):
        return [x.strip() for x in self.details.split(',')]

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('Backend', 'Backend Tips & Tutorials'),
        ('Data Engineering', 'Data Engineering Insights'),
        ('Data Analysis', 'Data Analyst Guides'),
        ('AI', 'AI & ML Innovations'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image_url = models.URLField(blank=True, null=True, help_text="URL for the blog category icon/image")
    link = models.URLField(help_text="Link to the full blog post")
    summary_points = models.TextField(help_text="Comma-separated summary points or highlights")

    def __str__(self):
        return f"{self.title} ({self.category})"

    def get_summary_list(self):
        return [x.strip() for x in self.summary_points.split(',')]
   

    


    
