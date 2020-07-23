# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, date 

# Create your models here.

class Goal(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    objective = models.CharField(max_length=50)
    key_result = models.CharField( max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.objective
    
    def save_goal(self):
        self.save
    
    def delete_goal(self):
        self.delete()