from django.db import models



class Player(models.Model):
    name = models.CharField(max_length = 20)
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to = 'player_images/')

    
