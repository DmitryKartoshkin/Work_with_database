from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    s = request.GET.get('sort')
    if s == 'name':
        phones = Phone.objects.order_by('name')
    elif s == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif s == 'min_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug=slug)
    for phone in phones:
        context = {'phone': phone}
    return render(request, template, context)
