from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #Ese foreignkey es para relacionar esa tabla con la de arriba
                                                                    #Ese on_delete=models.CASCADE es para que si la tabla anterior se borra lo que le siga a la relacionada tambien 
  