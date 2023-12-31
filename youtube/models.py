from django.db import models

class Video(models.Model):
	author = models.CharField(max_length = 200)
	title = models.CharField(max_length = 200)
	thumbnail = models.ImageField(upload_to='thumbnails/')
	icon = models.ImageField(upload_to='icons/')
	content = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title


class Comment(models.Model):
	name = models.CharField(max_length = 200)
	content = models.CharField(max_length=200)
	video = models.ForeignKey(Video, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.content
