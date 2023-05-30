from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'nikky','age':'10'}
    return render(request,'wish.html',context=d)
