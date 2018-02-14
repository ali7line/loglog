from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    topic_type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type')
    
    class Meta:
        ordering = ['-date_added', 'name']

    def __str__(self):
        return self.name


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'entries'

    def __str__(self):
        short_text = ''
        if len(self.text) < 50:
            short_text = self.text
        else:
            shor_text = self.text[:50] + '...'

        return "{}: {}".format(self.topic, short_text)
