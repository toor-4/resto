from django.shortcuts import render
from . forms import BookingForm
from . models import Menu

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
    context = {'form': form}
                         
    return render(request,'book.html', context)

def menu(request):
    data = Menu.objects.all()
    menu_data = {'menu' : data}
    
    return render(request,'menu.html', menu_data)

def menu_item(request,pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
        return render(request, 'menu_item.html', {'menu_item': menu_item} )

