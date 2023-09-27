from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "bike/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "home"
        return context
