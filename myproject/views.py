from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the API! Use /api/users/ to access the user endpoints.")
