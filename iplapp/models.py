from django.db import models
from django.utils import timezone

# Create your models here.

class Player(models.Model):
    jn = models.IntegerField(primary_key=True)  # Jersey Number
    pname = models.CharField(max_length=50)
    pteam = models.CharField(max_length=50)
    runs = models.IntegerField()
    wickets = models.IntegerField()
    # date_of_creation = models.DateTimeField()


    def __str__(self):
        return self.pname + " " + str(self.jn)