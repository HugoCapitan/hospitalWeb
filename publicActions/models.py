from django.db import models

class Announcement(models.Model):

	title = models.CharField(blank=False, max_length=100)
	content = models.TextField(blank=False)
	date = models.DateField(auto_now=True, blank=False)
	image = models.ImageField(blank=False, upload_to='announcements')

	class Meta:
		verbose_name = "Announcement"
		verbose_name_plural = "Announcements"

	def __str__(self):
		return self.content;
