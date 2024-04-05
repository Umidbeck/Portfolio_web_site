from django.shortcuts import render
from django.views.generic import DetailView
from .models import CV_Model, Portfolio_Model


# Create your views here.

def home_view(request):
    my_object = CV_Model.objects.get(id=1)  # Kerakli obyektni olish
    my_object_2 = Portfolio_Model.objects.all()
    context = {'object': my_object,
               'object_2': my_object_2,
               }
    return render(request, 'index.html', context)


class Portfolio_View(DetailView):
    model = Portfolio_Model
    queryset2 = CV_Model.objects.get(id=1)
    template_name = 'portfolio-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model2'] = self.queryset2
        return context