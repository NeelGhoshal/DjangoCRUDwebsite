from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Room(models.Model): #model for rooms present in website
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants = 
    updated = models.DateTimeField(auto_now=True) #timestamps are taken whenever updated
    created = models.DateTimeField(auto_now_add=True) #only takes time stamp only when created
    class Meta:         #for giving priority to order of data stored in the database based on type/time of creation
        ordering = ['-updated','-created']
    
    def __str__(self): #function for returing name of Room class
        return self.name 
    

    
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #user is imported from django prefabs
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #on_delete and cascade here means when parent i.e. room is deleted, all messages will be deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]  #Getting first 50 characters from the message


    
    
    
