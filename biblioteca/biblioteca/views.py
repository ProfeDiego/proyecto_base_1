from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name ='index.html'

class AcercaView(TemplateView):
    template_name ='acerca.html'
