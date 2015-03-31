from django.views.generic.base import TemplateView

from nightvision.models import Picture

from django.contrib.auth.decorators import login_required


#@login_required
class SliderView(TemplateView):

    template_name = "nightvision_frontend/slider.html"

    def get_context_data(self, **kwargs):
        context = super(SliderView, self).get_context_data(**kwargs)

        context['pictures'] = Picture.objects.all()

        return context
