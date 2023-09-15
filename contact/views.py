from django.shortcuts import render
from contact.forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
       # if form.is_valid():

    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})
