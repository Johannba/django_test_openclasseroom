from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Title

def about(request):
    return request('<h1>A propos<h1> <p>Nous adorons merch !</p>')

def listing(request):
     titles= Title.objects.all()
     return render(request,'listings/listings.html',
                   {'titles' :titles})         
 
def contact_us(request):
    contacts= '<h1>Contact us</h1>'
    return render(request,'listings/contact_us.html',
                   {'contacts':contacts})
 
def band_list(request): 
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',
           {'bands': bands})
   
def band_detail(request,id):
    band= Band.objects.get(id=id)
    return render(request,'listings/band_detail.html',
                  {'band':band})