from django.conf import settings 
from django.db import models 
from django.utils import timezone 


class Post(models.Model):
     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     title = models.CharField(max_length=200)
     text = models.TextField()
     created_date = models.DateTimeField(default=timezone.now)
     published_date = models.DateTimeField(blank=True, null=True)

     def publish(self):
         self.published_date = timezone.now()
         self.save()

     def __str__(self):
         return self.title
     

class MyTofI (models.Model):
    external_id = models.CharField(max_length=500, null=True, blank=True)

    content = models.TextField(null=False, blank=False, unique=True)

    class Meta:
        verbose_name_plural = ("MY Types of Intervention")

    def __str__(self):
        return self.content


class MyPriority (models.Model):
    external_id = models.CharField(max_length=500, null=True, blank=True)

    intervention_type = models.ManyToManyField(
        MyTofI, verbose_name="Type of Intervention", related_name="priorities", blank=True
    )
    class Meta:
        verbose_name_plural = ("MY Priority")


class MySOinP (models.Model):
    external_id = models.CharField(max_length=500, null=True, blank=True)

    priority = models.ForeignKey( 
        MyPriority, related_name="specific_objective_in_priority", on_delete=models.SET_NULL, null=True
    )
    
    intervention_type = models.ManyToManyField(
        MyTofI, verbose_name="Type of Intervention", related_name="specific_objective_in_priority", blank=True
    )
    class Meta:
        verbose_name_plural = ("MY SOinP")