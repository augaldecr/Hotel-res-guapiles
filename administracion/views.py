from django.shortcuts import render
from django.views.generic import CreateView
from .forms import FacturaForm, RegistroFormSet

# Create your views here.
class AddFacturaView(CreateView):
    template_name = 'create_factura.html'
    form_class = FacturaForm

    def get_context_data(self, **kwargs):
        context = super(AddFacturaView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = RegistroFormSet(self.request.POST)
        else:
            context['formset'] = RegistroFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())  # assuming your model has ``get_absolute_url`` defined.
        else:
            return self.render_to_response(self.get_context_data(form=form))