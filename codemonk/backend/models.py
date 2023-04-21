from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Paragraph(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()

    def __str__(self) -> str:
        return self.text


class Word(models.Model):
    word = models.TextField()
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    position = models.IntegerField()

    def __str__(self) -> str:
        return self.word
