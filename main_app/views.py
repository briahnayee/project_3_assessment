from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

def home(request):
  return render(request, 'home.html')

def items_index(request):
    items = Item.objects.all()
    print("items")
    return render(request, 'home.html', { 'items': items })

def item_create(request, post_it):
    form = ItemForm(request.POST)
    if form.is_valid():
        new_item = form.save(commit=False)
        new_item.save()
    return redirect('')


class ItemCreate(CreateView):
    model = Item
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ItemDelete(DeleteView):
    model = Item
    success_url = '/'