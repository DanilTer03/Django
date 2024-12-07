from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index2(request):
    return render(request, 'second_task/index2.html')


class index(TemplateView):
    def get(self, request):
        return render(request, 'second_task/index.html')