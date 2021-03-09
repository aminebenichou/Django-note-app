"""crudops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from ops import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('restApiOutput/', include('ops.urls')),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('postsignin/', views.postsignin),
    path('dashboard/', views.dashboard),
    path('savingNotes/', views.savingNotes),
    path('delete/id=<int:id>/', views.deleteNote, name='delete'),
    path('edit/id=<int:id>/', views.editNote, name='edit'),
    path('update/id=<int:id>/', views.updateNote, name='update'),
    path('logout/', views.logout_view, name='logout'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
