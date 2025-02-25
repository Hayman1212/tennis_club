
from django.http import HttpResponse
from django.template import loader
from .models import Member
import random



# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
                'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
  
  
def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
  
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

# def testing(request):
#     template = loader.get_template('template.html')
#     context = {
#         # 'fruits': ['Apple', 'Banana', 'Cherry'],  
#         'firstname': 'Linus', 
#     }
#     return HttpResponse(template.render(context, request))

def footer(request):
    template = loader.get_template('footer.html')
    return HttpResponse(template.render())


def testing(request):
    # mymembers = Member.objects.all().values()
    # mymembers = Member.objects.filter(lastname='Refsnes', id=2).values()
    # mymembers = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
    # mymembers = Member.objects.filter(firstname__startswith='L').values()
    # mymembers = Member.objects.all().order_by('-firstname').values()
    # mymembers = Member.objects.all().order_by('-id').values()

    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],  
        # 'mymembers': mydata,
        # 'mymembers': mymembers,
        # 'var1': 'John',
    #     # 'greeting': random.randint(1,3),
    #     # 'x': ['Apple', 'Banana', 'Cherry'],   
    #     # 'y': ['Apple', 'Banana', 'Cherry'], 
    #     'fruits': ['Apple', 'Banana', 'Cherry'],  
    }
    
    # context = {
    #     'cars': [
    #         {
    #             'brand': 'Ford',
    #             'model': 'Mustang',
    #             'year': '1964',
    #         },
    #         {
    #             'brand': 'Ford',
    #             'model': 'Bronco',
    #             'year': '1970',
    #         },
    #         {
    #             'brand': 'Volvo',
    #             'model': 'P1800',
    #             'year': '1964',
    #         }]
    #     }
    return HttpResponse(template.render(context, request))      