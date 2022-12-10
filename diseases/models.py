from django.db import models


class disease(models.Model):
    id=models.IntegerField(primary_key= True)
    Name=models.CharField(max_length=100)
    Details=models.TextField()
    Causes=models.TextField(null=True)
    Symptoms=models.TextField()
    Diagnosis=models.TextField(null=True)
    Treatment=models.TextField()
    image=models.ImageField(upload_to='photos/%y/%m/%d',null=True)
    def __str__(self):
        return self.Name

class dis_symptom(models.Model):
    title=models.CharField(max_length=100)
    symptom=models.TextField()
    def __str__(self):
        return self.title

class dis_cause(models.Model):
    title=models.CharField(max_length=100)
    cause=models.TextField()
    def __str__(self):
        return self.title

class dis_diagnosis(models.Model):
    title=models.CharField(max_length=100)
    diagnosis=models.TextField()
    def __str__(self):
        return self.title

class dis_treatment(models.Model):
    title=models.CharField(max_length=100)
    treatment=models.TextField()
    def __str__(self):
        return self.title
