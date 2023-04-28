from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime




# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.question_text
    
    @admin.display(
        boolean = True , 
        ordering = 'pub_date' , 
        description = "Published Recently?"
    )
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)




class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.choice_text} ===> {self.question}"




