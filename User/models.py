from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Jobs(models.Model):
    j_id=models.AutoField(primary_key=True)
    JobName=models.CharField(max_length=100, null=False)
    Salary=models.IntegerField(null=False)
    Experience=models.IntegerField(null=False)
    City=models.CharField(max_length=100, choices=(('Hyderabad', 'HYD'),('Mumbai', 'MUM'),('Chennai', 'CHN')), null=False)
    Skills=models.TextField(null=False)


    class Meta:
        db_table = "jobs"

    def __str__(self):
        return self.JobName

class Searches(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
   # j_name=models.CharField(Jobs, on_delete=models.CASCADE)

    class Meta:
        db_table = "searches"

    def __str__(self):
        return f"{self.user_id} - {self.j_name}"