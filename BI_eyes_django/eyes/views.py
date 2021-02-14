from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            form = UploadFileForm()
            # return HttpResponseRedirect('https://google.fr')
    else:
        form = UploadFileForm()
    return render(request, 'select.html', {'form': form})