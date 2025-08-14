from django.db import models


import string
import random

class ShortURL(models.Model):
	original_url = models.URLField()
	short_code = models.CharField(max_length=10, unique=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if not self.short_code:
			self.short_code = self.generate_short_code()
		super().save(*args, **kwargs)

	def generate_short_code(self, length=6):
		chars = string.ascii_letters + string.digits
		while True:
			code = ''.join(random.choices(chars, k=length))
			if not ShortURL.objects.filter(short_code=code).exists():
				return code
