from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Topic, Type
from .forms import TopicForm, TypeForm, TopicAddEntryForm


########################
# TOPIC
########################
class TopicList(ListView):
    template_name = 'logs/topic_list.html'
    model = Topic


class TopicDetail(DetailView):
    template_name = 'logs/topic_detail.html'
    model = Topic


class TopicCreate(CreateView):
    template_name = 'logs/topic_create.html'
    form_class = TopicForm


class TopicUpdate(UpdateView):
    template_name = 'logs/topic_update.html'
    form_class = TopicForm
    model = Topic


class TopicDelete(DeleteView):
    template_name = 'logs/topic_delete.html'
    model = Topic
    success_url = '/topic/'


class TopicAddEntry(CreateView):
    template_name = 'logs/topic_add_entry.html'
    model = Topic
    form_class = TopicAddEntryForm

####################
# TYPE
###################
class TypeList(ListView):
    template_name = 'logs/type_list.html'
    model = Type


class TypeDetail(DetailView):
    template_name = 'logs/type_detail.html'
    model = Type


class TypeCreate(CreateView):
    template_name = 'logs/type_create.html'
    form_class = TypeForm


class TypeUpdate(UpdateView):
    template_name = 'logs/type_update.html'
    model = Type
    form_class = TypeForm


class TypeDelete(DeleteView):
    template_name = 'logs/type_delete.html'
    success_url = '/type/'
    model = Type
