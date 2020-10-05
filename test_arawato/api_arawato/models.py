from django.db import models

# Create your models here.

class developer(models.Model):
    #id_developer lo genera auto django
    name_developer = models.CharField(max_length=100)

    def __str__(self):
        return self.name_developer

class console(models.Model):
    #id_console lo genera auto django
    name_console = models.CharField(max_length=100)
    release_date_console = models.DateField(blank=True ,null=True)

    def __str__(self):
        return self.name_console

class game(models.Model):
    title = models.CharField(max_length=100)
    release_date_game = models.DateField(blank=True, null=True)
    console = models.ForeignKey(console, on_delete=models.CASCADE)
    developer = models.ForeignKey(developer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title