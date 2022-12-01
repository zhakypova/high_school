from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО учителя')
    class_name = models.CharField(max_length=20,choices= (('a_class', 'a'),
                                                          ('b_class', 'b'),
                                                          ('c_class', 'c')),
                                  verbose_name='название класса')

    def __str__(self):
        return self.name

class Pupil(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО школьника')
    birth_date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




