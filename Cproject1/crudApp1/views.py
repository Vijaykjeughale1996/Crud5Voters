from django.shortcuts import render, redirect
from .models import voters
from .forms import votersForm

# Create your views here.
def votersView(request):
    form = votersForm()
    template_name = 'crudApp1/add.html'
    if request.method == 'POST':
        form = votersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def displayInfo(request):
    obj = voters.objects.all()
    template_name = 'crudApp1/display.html'
    context = {'data': obj}
    return render(request, template_name, context)

def updateInfo(request, pk):
    obj = voters.objects.get(ide = pk)
    form = votersForm(instance=obj)
    template_name = 'crudApp1/add.html'
    if request.method == 'POST':
        form = votersForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def deleteInfo(request, pk):
    obj = voters.objects.get(ide=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'crudApp1/confirm.html'
    context = {'data': obj}
    return render(request, template_name, context)