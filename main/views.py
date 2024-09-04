from django.shortcuts import render

def show_main(request):
    context = {
        'appname' : 'Easy Shop',
        'name': 'Muhammad Hibrizi Farghana',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
