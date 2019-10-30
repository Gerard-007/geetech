from django.views.generic import View
from django.shortcuts import render

class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')