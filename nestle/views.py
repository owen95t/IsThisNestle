from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Brand, Parent

# Create your views here.

# def index(request): #display all brands with no HTML
#     allBrands = Brand.objects.all()
#     output = '<pre>\n</pre> '.join([b.BRAND_NAME for b in allBrands])
#     # return HttpResponse("Hello, world. Youre at the IsThisNestle index.")
#     return HttpResponse(output)

def index(request):
    allBrands = Brand.objects.all()
    template = loader.get_template('nestle/index.html')
    context = {'allBrands': allBrands,}
    return HttpResponse(template.render(context, request))

def parent(request):
    allParent = Parent.objects.all()
    template = loader.get_template('nestle/parent.html')
    context = {'allParent': allParent,}
    return HttpResponse(template.render(context, request))

def detail(request, parent_id):
    return HttpResponse("You're looking at Parent: # %s" % parent_id)

def results(request, brand_id): #brand_id must be passed in URL
    response = "Youre looking at the subbrands: %s"
    return HttpResponse(response % brand_id)

def allbrands(request):
    try:
        brandList = Brand.objects.all()
    except Brand.DoesNotExist:
        raise Http404("BRAND DOES NOT EXIST")
    return render(request, 'nestle/allbrands.html', {'brand:': brandList})

def search(request):
    allInDB = Brand.objects.all()
    search_term = ''
    search_result = []
    if 'search' in request.GET:
        search_term = request.GET['search']
        search_result = Brand.objects.all().filter(BRAND_NAME__icontains=search_term)
        # search_result = Brand.objects.all().filter(PARENT_BRAND__PARENT_BRAND__icontains=search_term)

    context = {
        'search_term':search_term,
        'search_result':search_result,
        'allInDB':allInDB,
    }
    return render(request, 'nestle/search.html', context)
