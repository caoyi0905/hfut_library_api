from django.http import HttpResponse
from django.shortcuts import render
import model.findbooks as findbooks
import model.findstat as findstat

# Create your views here.
def lib(request):
    strText=request.GET.get('str')
    if type(strText)=='None':
        return HttpResponse('');
    page=request.GET.get('page')
    displaypg=request.GET.get('displaypg')
    return HttpResponse(findbooks.main(strText,page=page,displaypg=displaypg))

def marc(request,param):
    if type(param)=='None':
        return HttpResponse('')
    return HttpResponse(findstat.main(param))


def index(request):
    return HttpResponse('Hello,world!')