from django.shortcuts import render
from django.views.generic import View,TemplateView

# test : 1
# from django.http import HttpResponse
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL!!")


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'INJECTED CONTENT'
        context['inject_two'] = 'SECOND INJECT'
        context['you_too'] = 'WORLD IS IN LOVE...'
        return context
