from django.db import models

class CreateAccount(models.Model):
    firstName = models.CharField(max_length=100,blank=False)
    lastName = models.CharField(max_length=100,blank=False)
    emailId = models.EmailField(max_length=100,unique=True)
    mobileNumber = models.IntegerField(unique=True)
    address = models.TextField(max_length=250)

    def __str__(self):
        return(f"{self.firstName} {self.lastName} is trying to create a account with mobile number {self.mobileNumber}")
