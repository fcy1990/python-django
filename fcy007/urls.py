"""fcy007 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from app01 import views
from app01 import view

urlpatterns = [
    # path('admin/', admin.site.urls),
    # url('query', views.query),
    # url('add', views.add),
    # url('del', views.delete),
    # url('edit', views.edit),
    # url('student', views.query_student),
    # url('a_stu', views.add_student),
    # url('modal', views.modal_add_student),
    # url('update', views.modal_edit_student),
    # url('d_stu', views.modal_del_student),
    # url('teachers', views.query_teachers),
    # url('e-teacher',views.edit_teachers),
    # url('d-teacher',views.del_teachers),

    url(r'class',view.query_class),
    url(r'clas_add',view.add_class),
    url(r'clas_edit',view.edit_class),
    url(r'class_del',view.del_class),
]
