from django.db import models

# Create your models here.
class Buyer(models.Model): # модель представляющая покупателя.
    name = models.CharField(max_length=100) # покупателя(username аккаунта)
    balance = models.DecimalField(max_digits=150, decimal_places= 4)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Game(models.Model):  #модель представляющая игру.
    title = models.CharField(max_length=100) #название игры
    cost = models.DecimalField(max_digits=150, decimal_places= 4) # цена
    size = models.DecimalField(max_digits=150, decimal_places= 4) # размер файлов игры
    description = models.TextField() # описание(неограниченное кол-во текста)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='game')# - покупатель обладающий игрой. У каждого покупателя может быть игра и у каждой игры может быть несколько обладателей.
