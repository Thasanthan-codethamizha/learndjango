from django.db import models

# Create your models here.


class Bio(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.EmailField()
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.email
