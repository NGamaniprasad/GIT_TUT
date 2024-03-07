from django.db import models

# Create your models here.
class felt(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=200)
    location = models.TextField()

    def __str__(self):
        return self.name

class job(models.Model):
    job_role=models.CharField(max_length=120)
    location=models.CharField(max_length=122)
    salary=models.CharField(default=True,blank=False,max_length=12)

    def __str__(self):
        return self.salary