from django.shortcuts import render

def show_main(request):
    context = {
        'appname' : 'Easy Shop',
        'nama': 'Muhammad Hibrizi Farghana',
        'kelas': 'PBP A'
    }

    return render(request, "main.html", context)
