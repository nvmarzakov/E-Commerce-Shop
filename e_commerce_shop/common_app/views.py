from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from e_commerce_shop.common_app.forms import ContactForm


# Create your views here.
class AboutView(TemplateView):
    template_name = 'common/about.html'


class ContactView(View):
    template_name = 'common/contacts.html'

    def get(self, request):
        initial_data = {}
        if request.user.is_authenticated:
            initial_data['first_name'] = request.user.first_name  # Adjust this based on your User model
            initial_data['last_name'] = request.user.last_name  # Adjust this based on your User model
            initial_data['email'] = request.user.email

        form = ContactForm(initial=initial_data)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact submission to the database
            return redirect('common_app:contact-success-page')  # Redirect to a success page
        return render(request, self.template_name, {'form': form})


class ContactSuccessView(TemplateView):
    template_name = 'common/contact_success.html'
