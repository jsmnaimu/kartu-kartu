from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
            return self.title

class Card(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=124)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='img/%y', null=True, blank=True)
    is_baru = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Deck(models.Model):
    message = models.CharField(max_length=124)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='deck', default='1')

    def __str__(self):
            return self.message
