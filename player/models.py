from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    filename = models.CharField(max_length=255, default='default_filename.mp3')
    duration = models.CharField(max_length=10, default='0')
    audio_file = models.FileField(upload_to='music/', null=True, blank=True)  # New field

    def __str__(self):
        return f"{self.title} - {self.artist}"
