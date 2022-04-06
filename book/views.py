from django.shortcuts import redirect, render
from .models import Book

# Create your views here.
def create(request):
    if request.method == "POST":
        im = request.POST.get("impo")
        sn = request.POST.get("sname")
        su = request.POST.get("surl")
        sc = request.POST.get("scon")
        Book(site_name=sn, site_url=su, site_con=sc, impo=bool(im), user=request.user).save()
        return redirect("book:index")

    return render(request, "book/create.html")

def index(request):
    b = request.user.book_set.all()
    context = {
        "bset" : b
    }
    return render(request, "book/index.html", context)