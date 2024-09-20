from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='service_images/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.service.name} - {self.id}'

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    event_name = models.CharField(max_length=100)
    event_place = models.CharField(max_length=100)
    event_time = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.event_name}'
