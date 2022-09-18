"""job_board URL Configuration

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
from django.urls import path
from board import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/<int:id>', views.dashboard, name='dashboard'),
    path('signup/<int:id>', views.user_signup, name='signup'),
    path('login/<int:id>', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('addjob/<int:id>', views.add_job, name='add_job'),
    path('archievedjobs/<int:id>', views.archieved_jobs, name='archieved_jobs'),
    path('editjob/<int:id>/<int:jobid>', views.edit_job, name='edit_job'),
    path('archievejob/<int:id>/<int:jobid>', views.archieve_job, name='archieve_job'),
    path('deletejob/<int:id>/<int:jobid>', views.delete_job, name='delete_job'),
    path('applyjob/<int:id>/<int:jobid>', views.apply_job, name='apply_job'),
    path('checkoutjob/<int:id>/<int:jobid>', views.checkout_job, name='checkout_job'),
    path('candidates/<int:id>/<int:jobid>', views.candidates, name='candidates'),
]
