from django.http import JsonResponse
# Create your views here.

def root(request):
    context = {"status":"ok"}
    return JsonResponse(context)
