from django.db import models

class Todoapp(models.Model):
    content=models.TextField()