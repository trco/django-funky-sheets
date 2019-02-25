from extra_views import ModelFormSetView


class HotView(ModelFormSetView):

    action = 'create'
    button_text = 'Create'
    date_format = 'YYYY-MM-DD'
    errors_template = 'hot/errors.html'
    hot_template = 'hot/hot.html'
    hot_settings = {}

    # Add one minSpareRow for create action
    def get(self, request, *args, **kwargs):
        if self.action == 'create':
            self.hot_settings['minSpareRows'] = 1
        return super(HotView, self).get(request, *args, **kwargs)

    # Set number of extra forms in formset
    def get_factory_kwargs(self, **kwargs):
        factory_kwargs = super(HotView, self).get_factory_kwargs(**kwargs)
        if self.action == 'create':
            factory_kwargs['extra'] = 1
        else:
            factory_kwargs['extra'] = 0
        return factory_kwargs

    # Define queryset
    def get_queryset(self):
        if self.action == 'create':
            return self.model.objects.none()
        else:
            return super(HotView, self).get_queryset()

    # Add to the context
    def get_context_data(self, **kwargs):
        context = super(HotView, self).get_context_data(**kwargs)

        context['action'] = self.action
        context['button_text'] = self.button_text
        context['date_format'] = self.date_format
        context['hot_template'] = self.hot_template
        context['errors_template'] = self.errors_template
        context['hot_settings'] = self.hot_settings

        return context

    # Debug methods
    def formset_valid(self, formset):
        print("Form valid")
        return super(HotView, self).formset_valid(formset)

    def formset_invalid(self, formset):
        print("Form innnnnvalid")
        return super(HotView, self).formset_invalid(formset)
