from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        "variable1":"this is sent",
        "variable2":"saurav is great"
    }
    return render(request,'index.html',context)
    #return HttpResponse('This is Homepage')

def about(request):
    return HttpResponse('This is About page')

def services(request):
    return HttpResponse('This is Services page')

def contact(request):
    return HttpResponse('This is Contact page')