from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView


# Create your views here.
def home(request):
    return render(request, 'polls/base.html')
# class Home(TemplateView):
#     template_name = 'polls/base.html'

# class Contact(CreateView):
#     """Contact Page"""

#     model = Contact
#     form_class = HireForm
#     template_name = 'base/contact.html'

#     def form_valid(self, form):
#         contact = form.save()
#         contact.save()
#         messages.success(self.request, f'Your order has been sent! You would receive a reply shortly, thank you.')
#         return redirect('contact') 