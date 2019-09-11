from django.db import models

# Create your models here.

class Question(models.Model):
    question_name = models.CharField(max_length=100)
    question_type = models.CharField(max_length=100)
    question_text = models.TextField()
    
    def __str__(self):
            return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField()
    value = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
            return self.choice_text