from django.shortcuts import render
from .forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            return render(request, 'my_template.html', {'form': form, 'valid_url': form.cleaned_data['url']})
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})