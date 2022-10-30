from django.db import models

# category model
class Category(models.Model):
    title=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural ='Categories'

    def __str__(self):
        return self.title

# News model
class News(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='Imgs')
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural ='News'

    def __str__(self):
        return self.title
    
# comments Model

class Comment(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    comment=models.TextField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.comment 
    
# Contact Model
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    full_text = models.CharField(max_length=400)
    phone=models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    
    
# Teacher Model
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Imgs')
    bio = models.CharField(max_length = 200)
    pthone_number = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural ='Teachers'

    def __str__(self):
        return self.full_name
    
        
# Student Model
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Imgs')
    bio = models.CharField(max_length = 200)
    pthone_number = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural ='Students'

    def __str__(self):
        return self.full_name
    
    
    