from django.shortcuts import render


def about_view(request):
    return render(request, 'pages/about.html')

def contacts_view(request):
    return render(request, 'pages/contacts.html')

def privacy_view(request):
    return render(request, 'pages/privacy.html')

def terms_view(request):
    return render(request, 'pages/terms.html')

def faq_view(request):
    return render(request, 'pages/faq.html')