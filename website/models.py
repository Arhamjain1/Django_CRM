from django.db import models

#Creates databse from below models
class Record(models.Model): #Django plularises classs
    created_at=models.DateTimeField(auto_now_add=True) #Auot increment
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=50)

#Calling the reocrds in admin area or webpage will return the below
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")