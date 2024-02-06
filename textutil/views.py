#it is created my "shatrughan"
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'name':'Shatrughan','address':'Motibagh,Kishanganj'}
    return render(request,'index.html',params)

def analyze(request):
    # Get the text
    djtext=request.GET.get('text','default')
    #Check the values
    removepunc=request.GET.get('removepuch','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')

    if removepunc =='on':
        # analyzed=djtext
        #create a puncuation variable for puchuctaion store!
        puchutaions='''!()-[]{};:"'\,<>/.?@#$%^&*_~  '''
        analyzed=""
        for char in djtext:
            if char not in puchutaions:
                analyzed=analyzed+char
        params={'purpose':'After Remove Puncuation','analyzed_text':analyzed}
        djtext=analyzed

    if fullcaps =='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Upper case', 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremover =='on':
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]=="  ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Remove the extra space', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if ( extraspaceremover != 'on' and newlineremover !='on' and fullcaps !='on' and  removepunc !='on'):
        return HttpResponse("Error,Please! select any operation.")



    return render(request, "analyze.html", params)
