from django.urls import reverse
from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('logs:type_detail', kwargs={'type_slug': self.slug})


class Topic(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True)
    date_added = models.DateTimeField()
    topic_type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_added', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('logs:topic_detail', kwargs={'topic_slug': self.slug})


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'entries'

    def __str__(self):
        short_text = ''
        if len(self.text) < 50:
            short_text = self.text
        else:
            short_text = self.text[:50] + '...'

        return "{}: {}".format(self.topic, short_text)
