from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from members.models import Member
# Create your views here.

def home(request):
    return render(request, 'main.html')

def first_html(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def members_list(request):
    members = Member.objects.all().values()
    # print(members)
    return render(request, 'all_members.html', {'members': members})


def member_details(request, id):
    member = Member.objects.get(id=id)
    return render(request, 'member_details.html', {'member': member})


def testing(request):
    context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    }
    return render(request, 'template.html', context)