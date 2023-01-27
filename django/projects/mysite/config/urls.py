from django.contrib import admin
from django.urls import path, include
from pybo import views  # 더 이상 필요하지 않으므로 삭제

app_name = 'pybo'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')), 
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]