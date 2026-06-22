from django.shortcuts import render


app_name ="img"

def index(request):
    return render(request , 'base.html' , {})


def project_listing(request):
    return render(request , 'base.html' , {})

    
def project_detail(request):
    return render(request , 'base.html' , {})



def create_project(request):
    return render(request , 'base.html' , {})





