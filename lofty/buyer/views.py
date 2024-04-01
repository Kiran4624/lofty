from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def buyer_index_view(request):
    return HttpResponse( 'buyer side')



   
   