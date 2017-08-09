from django.shortcuts import render

def index(request):
    return render(request,'personal/home.html')


def contact(request):
    return render(request, 'personal/simple.html', {'content':['For contact,write an e-mail on:','stoqn780@gmail.com']})


