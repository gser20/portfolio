from django.db import models

class Project(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.description[:50]  # truncated description

class Inquiry(models.Model):
    # Define the fields for the Inquiry model here
    # For example:

    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
