from django.shortcuts import render


def index(request):
    text = 'Main page of site'
    context = {
        'text': text
    }
    return render(request, 'pages/index.html', context)


def page(request, page_slug):
    text = 'Page test_page/{}/ of site'.format(page_slug)
    context = {
        'text': text,
        'page_slug': page_slug
    }
    return render(request, 'pages/page.html', context)
