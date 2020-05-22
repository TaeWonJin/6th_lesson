from django.db import models

class youtube(models.Model):
    name = models.CharField(max_length = 50)
    creator = models.CharField(max_length=20)
    recommend = models.IntegerField(default=0)
    on_off = models.BooleanField(default=True)
    subscribe_num = models.IntegerField(default=0)
    youtube_link_1 = models.TextField(max_length=100)
    youtube_link_2 = models.TextField(max_length=100)
    youtube_link_3 = models.TextField(max_length=100)
    text = models.TextField(max_length=2000)
    summary = models.TextField(max_length=200)
    photo = models.ImageField(upload_to="image",blank=True)

    def __str__(self):
        return '%s' %(self.name)