from django.shortcuts import render
# функция render по-умолчанию будет искать файлы в папке templates


def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')
