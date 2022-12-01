from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name='название курсов')
    mentor = models.CharField(max_length=20, verbose_name='имя ментора')
    month = models.IntegerField(default=6,verbose_name= 'длительность курсов')

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20, verbose_name='фио студента')
    laptop = models.CharField(max_length=20, choices=(
        ('mac', 'MacBook'),('linux', 'Linux'),('windows', 'Windows')
    ), verbose_name='операционная система')

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
