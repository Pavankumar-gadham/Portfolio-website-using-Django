from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    projects_show = [
        {"title":"Heart Disease Prediction",
         "path":"images/heart.jpeg",
         "description":"A project that predicts heart disease using machine learning algorithms."},
        
        {"title":"Hardware Hub",
         "path":"images/hardwarehub.jpeg",
        "description": "A platform for purchasing the custom PC's."},

        {"title":"E-commerce Shopping Website",
         "path":"images/shopping.jpeg",
        "description":"An online shopping website with features like product search and checkout."},

        
        {"title":"Image Search Website",
         "path":"images/imagesearch.jpeg",
        "description": "A website that allows users to search for images based on keywords."}

    ]
    return render(request, "projects.html", {"projects_show":projects_show})


def certificates(request):
    return render(request, "certificates.html")

def contact(request):
    return render(request, "contact.html")

def resume(request):
    resume_path = "myapp/PAVAN KUMAR GADHAM.PDF"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['content_Disposition'] = 'attachment';filename="PAVAN KUMAR GADHAM.pdf"
            return response
        
    else:
        return HttpResponse("resume not found", status=404)