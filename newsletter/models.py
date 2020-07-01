from django.db import models

# Create your models here.
class signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.email