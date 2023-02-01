"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from quiz.views import *
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('', home, name='home'),
    path('addQuiz/', addQuiz, name='addQuiz'),
    path('addQuestions/<int:quiz_id>/', addQuestion, name='addQuestion'),
    path("<int:quiz_id>/", displayQuiz, name="displayQuiz"),

    path('myquizzes/', myquizzes, name='myquizzes'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('register/', registerPage, name='register'),
    path('admin/', admin.site.urls),
 
]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
