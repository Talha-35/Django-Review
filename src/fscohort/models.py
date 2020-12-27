from django.db import models

# Create your models here.

# Allatki kod ile tablomuzu admin kısmında gösterebiliyoruz
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()


    def __str__(self):
        return self.first_name +" "+  self.last_name
        # Buraya tabloda ne gözükmesini istiyor isek o şekilde yazabiliriz
        # return str(self.number)

        # return "{} {}".format(self.first_name, self.last_name)

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()


    def __str__(self):
        return self.first_name +" "+  self.last_name