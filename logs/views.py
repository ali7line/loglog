from django.shortcuts import render
from django.views.generic import View

from .models import Topic


class TopicList(View):
    template_name = 'logs/topic_list.html'
    model = Topic

    def get(self, request):
        return render(request, self.template_name, {'topic_list': self.model.objects.all()})
