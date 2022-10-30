from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('all-news',views.all_news,name='all-news'),
    path('all-teachers',views.all_teachers,name='all-teachers'),
    path('all-students',views.all_students,name='all-students'),
    path('faoliyat',views.faoliyat,name='faoliyat'),
    path('kafedra',views.kafedra,name='kafedra'),
    path('detail/<int:id>',views.detail,name="detail"),
    path('contact',views.contact,name = "contact"),
    # path('category/<int:id>',views.category,name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)