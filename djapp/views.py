from django.http import HttpResponse

def index(request):
    print("Welcome to Azure app aservice with az_pipeline")
    return HttpResponse("Hello from Django!")
