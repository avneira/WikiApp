from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import article, theme


# Home view, obtiene la informacion de article 
def home(request):
    articleTotal = article.objects.all()
    return render(request, 'home.html',{
        'listaArticle' : articleTotal
    })


# New Theme: 
# si se obtiene el method = POST, se almacenan la informacion recibida
def newTheme(request):
    if request.method == 'POST':
        nameTheme = request.POST.get('nameTheme')
        descriptionTheme = request.POST.get('descriptionTheme')
        
        # la informacion almacenada se guarda en las variables del model theme
        theme.objects.create(
            nameTheme=nameTheme,
            descriptionTheme=descriptionTheme
        )
        #se redirige a la misma pagina 
        return HttpResponseRedirect(reverse('wikiPy:newTheme'))
    
    return render(request, 'newTheme.html')


# si se obtiene el method = POST, se almacenan la informacion recibida
def newArticle(request):
    if request.method=='POST':
        nameArticle = request.POST.get('nameArticle')
        contentArticle = request.POST.get('contentArticle')

        areaSeleccionada= request.POST.get('areaSeleccionada')
        themeObj = theme.objects.get(id=areaSeleccionada)

        #la informacion almacenada se guarda en las variables del model article
        article.objects.create(
            nameArticle=nameArticle,
            contentArticle=contentArticle,
            themeR = themeObj
        )
        #al crearse la variable, se redirige a la misma pagina  de crear nuevo articulo 
        return HttpResponseRedirect(reverse('wikiPy:newArticle'))
    
    return render(request, 'newArticle.html',{
        'listTheme' : theme.objects.all()
    })



def themeList(request):
    themeTotal = theme.objects.all()
    return render(request, 'themeList.html',{
        'listTheme' : themeTotal
    })



def articlesByTheme(request, idTheme):
    infoTheme = theme.objects.get(id=idTheme)
    listArticle = infoTheme.article_set.all()

    return render(request, 'articlesByTheme.html',{
        'objetoTheme':infoTheme,
        'listTheme': theme.objects.all(),
        'listArticle' :listArticle

    })

def view_article(request, idArticle):
    infoArticle = article.objects.get(id=idArticle)
    
    return render(request, 'view_article.html',{
        'objArticle':infoArticle,
        'listArticle' : theme.objects.all()
    }) 
