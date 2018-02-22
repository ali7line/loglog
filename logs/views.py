from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import Topic, Type
from .forms import TopicForm, TypeForm, TopicAddEntryForm
from .utils import ObjectListViewMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin


########################
# TOPIC
########################
class TopicList(ObjectListViewMixin, View):
    template_name = 'logs/topic_list.html'
    model = Topic


class TopicDetail(View):
    template_name = 'logs/topic_detail.html'
    model = Topic

    def get(self, request, slug):
        topic = get_object_or_404(self.model, slug=slug)
        entries = topic.entry_set.all()
        context = {'topic': topic, 'entries': entries}
        return render(request, self.template_name, context)


class TopicCreate(ObjectCreateMixin, View):
    template_name = 'logs/topic_create.html'
    form_class = TopicForm


class TopicUpdate(ObjectUpdateMixin, View):
    template_name = 'logs/topic_update.html'
    form_class = TopicForm
    model = Topic


class TopicDelete(ObjectDeleteMixin, View):
    template_name = 'logs/topic_delete.html'
    model = Topic
    success_url = '/topic/'


class TopicAddEntry(View):
    template_name = 'logs/topic_add_entry.html'
    model = Topic
    form_class = TopicAddEntryForm

    def get(self, request, slug):
        topic = get_object_or_404(self.model, slug=slug)
        return render(request, self.template_name, {'form': self.form_class(), 'topic': topic})

    def post(self, request, slug):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_topic = bound_form.save()
            return redirect(new_topic)
        else:
            return render(request, self.template_name, {'form': bound_form})

####################
# TYPE
###################


class TypeList(ObjectListViewMixin, View):
    template_name = 'logs/type_list.html'
    model = Type


class TypeDetail(View):
    template_name = 'logs/type_detail.html'
    model = Type

    def get(self, request, type_slug):
        type_ = get_object_or_404(self.model, slug=type_slug)
        topics = type_.topic_set.all()
        number = len(topics)
        context = {'type': type_, 'topics': topics, 'number': number}
        return render(request, self.template_name, context)


class TypeCreate(ObjectCreateMixin, View):
    template_name = 'logs/type_create.html'
    form_model = TypeForm


class TypeUpdate(ObjectUpdateMixin, View):
    pass


class TypeDelete(ObjectDeleteMixin, View):
    pass
