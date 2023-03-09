from django.db import models

# Create your models here.
class position(models.Model):
    title=models.CharField(max_length=50)
     
    def __str__(self):
        return self.title
    

class employee(models.Model):
    FullName=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=3)
    mobile_no=models.CharField(max_length=10)
    position=models.ForeignKey(position,on_delete=models.CASCADE)

    def __str__(self):
        return self.FullName

    
    

    


    
