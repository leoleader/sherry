from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
 
class addQuestionform(ModelForm):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    class Meta:
        model=QuesModel
        fields="__all__"
        exclude = ['quiz']

    def __init__(self, *args, **kwargs):
        super(addQuestionform, self).__init__(*args, **kwargs)
        self.fields['op3'].required = False
        self.fields['op4'].required = False

class addPersform(ModelForm):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    class Meta:
        model=PersModel
        fields="__all__"
        exclude = ['quiz']
    def __init__(self, *args, **kwargs):
        super(addPersform, self).__init__(*args, **kwargs)
        

class addQuizform(ModelForm):
    class Meta:
        model=QuizModel
        fields="__all__"
        exclude = ['creator']
    def __init__(self, *args, **kwargs):
        self.creator = 'creator'
        super(addQuizform, self).__init__(*args, **kwargs)

class addPersonalityform(ModelForm):
    class Meta:
        model=Personality
        fields="__all__"
        exclude = ['quiz']





