


from django.views.generic import View

from django.shortcuts import render

# url:localhost:8000/helloworld
# method:get

class HelloWorldView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"helloworld.html")
    
class GoodMOrningView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"morning.html")
    

# url:localhost:8000/actor1/
# url:localhost:8000/actor2/
# url:localhost:8000/actor3/
# url:localhost:8000/actor4/
# url:localhost:8000/actor5/

class SachinView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"sachin.html")