from multiprocessing import Condition
from django.db import models

# Create your models here.


class Table1(models.Model):
    InspectionID = models.IntegerField(primary_key=True)
    PipeID = models.CharField(max_length=6)
    Length = models.IntegerField(default=0)
    Width = models.IntegerField(default=0)
    Rating = models.IntegerField(default=0)

    def __str__(self):
        return str(self.InspectionID)


class Table2(models.Model):
    ConditionID = models.IntegerField(primary_key=True)
    InspectionID = models.ForeignKey(Table1, on_delete=models.CASCADE)
    Distance = models.IntegerField(default=0)
    Code = models.CharField(max_length=3)

    def __str__(self):
        return str(self.ConditionID)
