from django.shortcuts import render
from .models import Skill,Login
# Create your views here.

def main_page(request):
    x = Skill.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        messege = request.POST.get('text')
        data = Login(email = email, messege = messege)
        data.save()
    
    return render(request,'portfolio.html',{'skills':x})