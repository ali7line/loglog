from django.shortcuts import render, redirect, get_object_or_404


class ObjectListViewMixin:
    template_name = ''
    model = None

    def get(self, request):
        context = {self.model.__name__.lower()+'_list': self.model.objects.all()}
        return render(request, self.template_name, context)


class ObjectCreateMixin:
    template_name = ''
    form_model = None

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_model()})

    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            new_topic = bound_form.save()
            return redirect(new_topic)
        else:
            return render(request, self.template_name, {'form': bound_form})


class ObjectUpdateMixin:
    template_name = ''
    model = None
    form_model = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug)
        context = {
                'form': self.form_model(instance=obj),
                self.model.__name__.lower(): obj,
                }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug)
        bound_form = self.form_model(request.POST, instance=obj)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                    'form': bound_form,
                    self.model.__name__.lower(): obj,
                    }
            return(request, self.template_name, context)


class ObjectDeleteMixin:
    success_url = ''
    template_name = ''
    model = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug)
        return render(request, self.template_name, {self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug)
        obj.delete()
        return redirect(self.success_url)
