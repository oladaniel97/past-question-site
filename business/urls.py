from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('department/<int:id>',views.department,name='department'),
    path('course/<int:id>',views.course,name='course'),
    path('past_question/<int:id>',views.past_questions,name='past_questions'),
    path('past_detail/<int:id>',views.past_details,name='past_detail'),
    path('about',views.about,name='about'),
    path('search',views.search,name='search')
]