from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.contrib import messages

class SuccessView(TemplateView):
    template_name = 'success.html'

class ProfileFormView(FormView):
    form_class = ProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        profile = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'В поле {field} возникла ошибка: {error}')
        return super().form_invalid(form)