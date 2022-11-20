from django.shortcuts import render
def ihome(request):
    return render(request, 'test.html')
# Create your views here.
def ilina(request):
    print(request)
    name=request.GET.get('name')
    print(name)
    familia=request.GET.get('fameliiiiiia')
    print(familia)
    nupzh=request.GET.get('nupzh')
    print(nupzh)
    return render(request, 'test01.html',{"uzbek":name,"privet":familia,"abhazia":nupzh})
