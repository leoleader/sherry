from django.db import models

# Create your models here.
from django.contrib.auth.models import *

class QuizModel(models.Model):
    title = models.CharField(max_length = 100, null = True)
    blurb = models.CharField(max_length = 600, null = True)
    cover = models.ImageField(upload_to='images/', null=True, blank=True, default='images/quiz-photo.jpeg')

    knowledge = "knowledge"
    personality = "personality"
    types = [(knowledge, "Knowledge"), (personality, "Personality")]

    quiz_type = models.CharField(
        max_length=15,
        choices=types,
        default=knowledge
    )

    creator = models.ForeignKey(User, unique=False, on_delete = models.CASCADE, default=1)

    def __str__(self):
        return self.title
    

class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True, blank=True, default='')
    op4 = models.CharField(max_length=200,null=True, blank=True, default='')
    ANSWER_CHOICES = [('option1', 'op1'), ('option2', 'op2'), ('option3', 'op3'), ('option4', 'op4')]
    ans = models.CharField(choices=ANSWER_CHOICES, max_length=200,null=True)

    quiz = models.ForeignKey(QuizModel, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.question

class Personality(models.Model):
    title = models.CharField(max_length=200,null=True)
    blurb = models.CharField(max_length = 600, null = True)
    quiz = models.ForeignKey(QuizModel, on_delete = models.CASCADE)
    ## eventually gonna include options for user uploaded image

    def __str__(self):
        return self.title

class PersModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True, blank=True, default='')
    op4 = models.CharField(max_length=200,null=True, blank=True, default='')
    quiz = models.ForeignKey(QuizModel, on_delete = models.CASCADE)

    ans1 = models.CharField(max_length=200,null=True)
    ans2 = models.CharField(max_length=200,null=True)
    ans3 = models.CharField(max_length=200,null=True, blank=True, default='')
    ans4 = models.CharField(max_length=200,null=True, blank=True, default='')
    
    def __str__(self):
        return self.question
    


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    fullname = models.CharField('Full Name', max_length=50)
    birthdate = models.DateTimeField('Birthday')
    url = models.URLField('Website', blank=True)
    picture = models.ImageField('Picture/Avatar', upload_to='img/users/profile', blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.user


