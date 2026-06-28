
from django.urls import path

from members import views

urlpatterns = [
    path('testing/', views.testing),
    path('first_html/', views.first_html),
    path('members/', views.members_list, name = "members"),
    path('members/details/<slug:slug>/', views.member_details, name = "member_details"),
    path('with-tag', views.with_tag),
    path('operators', views.operators),
]