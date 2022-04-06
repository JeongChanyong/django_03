from django.shortcuts import render
import pdfplumber
# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        # print(request.POST)
        p = request.FILES.get("pdf")
        if p:
            pdf = pdfplumber.open(p)
            num = len(pdf.pages)
            st = ""
            for i in range(num):
                st += "="*30 + "\n"
                st += f"{i+1} PAGES TEXT" + "\n"
                st += "="*30 + "\n"
                st += pdf.pages[i].extract_text() + "\n\n"

            context.update({
                "st" : st
            })

    return render(request, "pdfread/index.html", context)




# ctrl + shift + P    >    select interpreter     >  python 버전 세팅





  



