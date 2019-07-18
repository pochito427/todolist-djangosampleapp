from django.db import models

#objects = models.Manager()
# Create your models here.
class  Task(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    estimated_time = models.IntegerField(default=1)
    worked_time = models.FloatField(default=0.0)
    difference_time = models.IntegerField(default=1)
    


    def __str__(self):
        return self.title + ' | ' + self.description + ' | ' + str(self.estimated_time) + ' | ' + str(self.worked_time) + ' | ' + str(self.difference_time)