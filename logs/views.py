from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import Topic, Type
from .forms import TopicForm, TypeForm, TopicAddEntryForm


class TopicList(View):
    template_name = 'logs/topic_list.html'
    model = Topic

    def get(self, request):
        return render(request, self.template_name, {'topic_list': self.model.objects.all()})


class TopicDetail(View):
    template_name = 'logs/topic_detail.html'
    model = Topic

    def get(self, request, topic_slug):
        topic = get_object_or_404(self.model, slug=topic_slug)
        entries = topic.entry_set.all()
        context = {'topic': topic, 'entries': entries}
        return render(request, self.template_name, context)


class TopicCreate(View):
    template_name = 'logs/topic_create.html'
    form_class = TopicForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_topic = bound_form.save()
            return redirect(new_topic)
        else:
            return render(request, self.template_name, {'form': bound_form})


class TopicAddEntry(View):
    template_name = 'logs/topic_add_entry.html'
    model = Topic
    form_class = TopicAddEntryForm

    def get(self, request, topic_slug):
        topic = get_object_or_404(self.model, slug=topic_slug)
        return render(request, self.template_name, {'form': self.form_class(), 'topic': topic})

    def post(self, request, topic_slug):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_topic = bound_form.save()
            return redirect(new_topic)
        else:
            return render(request, self.template_name, {'form': bound_form})


class TypeList(View):
    template_name = 'logs/type_list.html'
    model = Type

    def get(self, request):
        return render(request, self.template_name, {'type_list': self.model.objects.all()})


class TypeDetail(View):
    template_name = 'logs/type_detail.html'
    model = Type

    def get(self, request, type_slug):
        type_ = get_object_or_404(self.model, slug=type_slug)
        topics = type_.topic_set.all()
        number = len(topics)
        context = {'type': type_, 'topics': topics, 'number': number}
        return render(request, self.template_name, context)


class TypeCreate(View):
    template_name = 'logs/type_create.html'
    form_model = TypeForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_model()})

    def post(self, request):
        bounded_form = self.form_model(request.POST)
        if bounded_form.is_valid():
            new_type = bounded_form.save()
            return redirect(new_type)
        else:
            return render(request, 'logs/type_create.html', {'form': bounded_form})
