from django.db import models

# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	mucdo = models.CharField(max_length=20, choices=[('0','rất gấp'),('1','gấp'),('2','không gấp')], verbose_name='Mức Độ')
	ngayhoanthanh = models.DateField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
