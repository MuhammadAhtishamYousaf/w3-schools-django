
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q, QuerySet


from members.models import Member



def home(request):
    return render(request, 'main.html')

def first_html(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def members_list(request):
    # members = Member.objects.all() # All records
    # members = Member.objects.all().values_list('id', 'first_name') #Records only id and first_name column
    # members = Member.objects.all().values() # All records, but list[dic] (python dict)
    
    #And
    # members = Member.objects.filter(first_name='Ahtisham', last_name='Yousaf') 
    
    #Or
    # members = Member.objects.filter(first_name='Ahtisham') | Member.objects.filter(last_name='Yousaf')
    # members = Member.objects.filter(Q(first_name='htisham') | Q(last_name="Yousaf"))
    
    # Field Lookups (Like)
    # members = Member.objects.filter(first_name__startswith='A') # Like A%
    # members = Member.objects.filter(first_name__startswith='A').values()
    # members = Member.objects.filter(first_name__contains='ham') # case sensitive Like %ham%
    # members = Member.objects.filter(first_name__icontains='ham') # case insensitive Like %ham%
    
    # Order by 
    # members = Member.objects.all().order_by('last_name').values() # Asc
    
    members = Member.objects.all().order_by('-first_name')
    
    
    print(members)
    return render(request, 'all_members.html', {'members': members})


def member_details(request, slug):
    # member = Member.objects.get(id=id)
    member = Member.objects.filter(slug=slug).first()
    print(member)
    return render(request, 'member_details.html', {'member': member})


def testing(request):
    context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    }
    return render(request, 'template.html', context)

def with_tag(request):
    return render(request, 'with_tag.html' )


def operators(request):
    context = {
        'greeting': 2,
        'day': 'Friday',
        'fruits': ['Apple', 'Banana', 'Cherry'],
        'member': None,
    }
    return render(request, 'operators.html', context)