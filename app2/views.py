from django.shortcuts import render

# Create your views here.
def second(request):
    d={'name':'manasareddy','mobile':56433546564,'age':22}
    return render(request,'second.html',d)
