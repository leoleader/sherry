from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
 
# Create your views here.
def home(request):
    if request.method == 'POST':
        quizzes=QuizModel.objects.all()
        return render(request,'result.html',context)
    else:
        quizzes=QuizModel.objects.all()
        context = {
            'quizzes':quizzes
        }
        return render(request, 'home.html', context)

def displayQuiz(request, quiz_id):
    print(request.POST)
    quiz_model = QuizModel.objects.get(id = quiz_id)
    quiz_type = quiz_model.quiz_type
    if (quiz_type == "knowledge"):
        questions = QuesModel.objects.filter(quiz_id = quiz_id)
        context = {
            'questions':questions,
            'quiz':quiz_model
        }
        if request.method == 'POST':
            score=0
            wrong=0
            correct=0
            total=0
            for q in questions:
                total+=1
                if (q.ans == request.POST.get(q.question)):
                    score += 1
                    correct += 1
                else:
                    wrong += 1
            percent = (score / total) * 100
            print(percent)
            context = {
                'score':score,
                'correct':correct,
                'wrong':wrong,
                'percent':percent,
                'total':total
            }
            return render(request,'result.html',context)
        else:
            print("ruh roh")
            return render(request, 'displayquiz.html', context)
    else:
        questions = PersModel.objects.filter(quiz_id = quiz_id)
        context = {
            'questions':questions,
            'quiz':quiz_model
        }
        if request.method == 'POST':
            personalitys = Personality.objects.filter(quiz_id = quiz_id)
            totaler = {}
            for i in personalitys:
                totaler[i.title] = 0
            for q in questions:
                answered_pers = request.POST.get(q.question)
                if answered_pers == "option1":
                    totaler[q.ans1] += 1
                elif answered_pers == "option2":
                    totaler[q.ans2] += 1
                elif answered_pers == "option3":
                    totaler[q.ans3] += 1
                else:
                    totaler[q.ans4] += 1
            final = max(totaler, key = totaler.get)
            final_pers = Personality.objects.get(title = final, quiz_id = quiz_id)
            title = final_pers.title
            blurb = final_pers.blurb
            context = {
                'final':final,
                'title':title,
                'blurb':blurb
            }
            return render(request,'persresult.html',context)
        else:
            print("yay")
            return render(request, 'displayquiz.html', context)

 
def addQuestion(request, quiz_id):
    quiz = get_object_or_404(QuizModel, pk=quiz_id)
    questions = QuesModel.objects.filter(quiz_id = quiz_id)
    context = {'questions':questions}    
    if request.user.is_authenticated:
        if quiz.quiz_type == "knowledge":
            if(request.method=='POST'):
                form = addQuestionform(request.POST)
                m = form.save(commit=False)
                m.quiz = quiz
                m.save()
            return render(request,'addQuestion.html', context)
        else:
            if(request.method=='POST'):
                print(request.POST)
                formy=addPersform(request.POST)
                if 'addpersonality' in request.POST:
                    print("yuh")
                    form = addPersonalityform(request.POST, quiz)
                    m = form.save(commit=False)
                    m.quiz = quiz
                    m.save()
                    personalities = Personality.objects.filter(quiz_id = quiz_id)
                    context={'form':formy, 'quiz_id':quiz_id, 'personalities':personalities}
                    return render(request,'addPers.html', context)
                elif 'addquestion' in request.POST:
                    print("bruh")
                    form = addPersform(request.POST)
                    print(form)
                    m = form.save(commit=False)
                    m.quiz = quiz
                    m.save()
                    personalities = Personality.objects.filter(quiz_id = quiz_id)
                    context={'form':addPersform(), 'quiz_id':quiz_id, 'personalities':personalities}
                    return render(request,'addPers.html', context)
            else:
                form=addPersform()
                context={'form':form, 'quiz_id':quiz_id}
                return render(request,'addPers.html', context)
            return render(request,'addPers.html')
    else: 
        return redirect('home') 

def addQuiz(request):    
    if request.user.is_authenticated:
        form=addQuizform()
        if(request.method=='POST'):
            form=addQuizform(request.POST, request.FILES)
            print(form)
            if(form.is_valid()):
                print(request.FILES)
                m = form.save(commit = False)
                print('checkmark')
                print(m.cover)
                m.save()
                return redirect('/addQuestions/' +str(m.id))
        context={'form':form, 'creator':request.user}
        return render(request,'addQuiz.html',context)
    else: 
        return redirect('home') 

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')

def myquizzes(request):
    if request.user.is_authenticated:
        quizzes=QuizModel.objects.filter(creator = request.user)
        context = {
                'quizzes':quizzes
        }
        return render(request, 'myquizzes.html', context)
    else: return redirect('home')