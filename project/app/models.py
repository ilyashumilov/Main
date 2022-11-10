from django.db import models

class Area(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Curator(models.Model):
    name = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + 'curator of' + str(self.area) + 'area'

class Discipline(models.Model):
    title = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title) + 'of area' + str(self.area.title)

class Group(models.Model):
    title = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title) + 'of area' + str(self.area.title)

class Student(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sex) + ' ' + str(self.name) + 'of group' + str(self.group.title)