from django.db import models
# Create your models here.
class myuser(models.Model):
    gender = (
        ("male","男"),
        ("female","女"),
    )
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    time = models.DateTimeField(auto_now_add=True)
    sex = models.CharField(max_length=20,choices = gender,default="男")

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"