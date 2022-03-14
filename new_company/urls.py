from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('form/', views.form),
    path('employees/', views.employees_view,name="all_employees"),
    path('employees/<int:id>/', views.detail_view, name="detail_view"),
    path('employees/<int:id>/delete/', views.delete_view),
    path('create_employee/', views.create_view),
    path("employees/<int:id>/update/", views.update_view)
]