


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
    

# url:localhost:8000/selfinro/
# method:get

class SelfintroView(View):

    def get(self,request,*args,**kwargs):

        context={
            "name":"ABIJITH",
            "title":"web developer",
            "email":"abijith@gmail.com"
        }

        return render(request,"selfintro.html",context)


class MobileListView(View):

    def get(self,request,*args,**kwargs):

        # context={
        #     "name":"MotoEdge60",
        #     "price":"25000",
        #     "brand":"moto",
        #     "display":"amoled"
        # }

        data=[

            {"id":1,"name":"edge60","price":24000},
            {"id":2,"name":"edge50","price":22000},
            {"id":3,"name":"edge60pro","price":27000},

        ]

        

        return render(request,"mobile_list.html",{"mobiles":data})
    



class RecepieListView(View):

    def get(self,request,*args,**kwargs):

        data=[
            {"id":1,"name":"friedrice","ingradients":"rice,onion,egg,chicken,beans,carrot"},
            {"id":2,"name":"gheeedrice","ingradients":"rice,onion,egg,chicken,beans,carrot"},
            {"id":3,"name":"arabian rice","ingradients":"rice,onion,egg,chicken,beans,carrot"},
            {"id":4,"name":"dosa","ingradients":"rice,onion,egg,chicken,beans,carrot"},
            {"id":5,"name":"porotta","ingradients":"rice,onion,egg,chicken,beans,carrot"},
            {"id":6,"name":"banana fry","ingradients":"rice,onion,egg,chicken,beans,carrot"}

        ]


        return render(request,"recepie_list.html",{"recepies":data})



