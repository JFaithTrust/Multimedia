from django.shortcuts import render,redirect
from django.contrib import messages
from .models import News,Category,Comment,Contact,Teacher,Student

#  Home Page
def home(request):
    first_news=News.objects.first()
    three_news=News.objects.all()[1:4]
    three_categories=Category.objects.all()[0:3]

    return render(request, 'home.html',{
        'first_news':first_news,
        'three_news':three_news,
        'three_categories':three_categories
    })
    
def home_2(request):
    all_teachers=Teacher.objects.all()
    return render(request, 'home.html',{
        'all_teachers':all_teachers
    })

# All News Page
def all_news(request):
    all_news=News.objects.all()
    return render(request, 'all-news.html',{
        'all_news':all_news
    })
    
# Teachers page
def all_teachers(request):
    all_teachers=Teacher.objects.all()
    return render(request, 'all-teachers.html',{
        'all_teachers':all_teachers
    })
    
# Students page
def all_students(request):
    all_students=Student.objects.all()
    return render(request, 'all-students.html',{
        'all_students':all_students
    })


# Deatil Page
def detail(request,id):
    news=News.objects.get(pk=id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        comment=request.POST['message'] 
        Comment.objects.create(
            news=news,
            name=name,
            email=email,
            comment=comment
        )
    messages.success(request,'comment submitted but in moderation mode.')
    category=Category.objects.get(id=news.category.id)
    rel_news=News.objects.filter(category=category).exclude(id=id)
    comments=Comment.objects.filter(news=news,status=True).order_by('-id')
    return render(request, 'detail.html',{
        'news':news,
        'related_news':rel_news,
        'comments':comments
    })
    
def contact(request):
    if request.method=='POST':
        full_name=request.POST['full_name']
        email=request.POST['email']
        phone=request.POST['phone']
        title=request.POST['title']
        full_text=request.POST['full_text'] 
        Contact.objects.create(
            full_name=full_name,
            email=email,
            phone = phone,
            title=title,
            full_text=full_text
        )
        messages.success(request,'Contact submitted but in moderation mode.')
    return render(request, 'contact.html')

def faoliyat(request):
    return render(request, 'faoliyat.html')

def kafedra(request):
    return render(request, 'kafedra.html')
