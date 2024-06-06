from django.shortcuts import render, redirect
from . forms import ReservationForm
from . models import Menu

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def submit_reservation(request):
    form = ReservationForm() 
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') # Redirect to a success page

    context = {'form': form}

    if form.errors:
        print(form.errors)  # Print form errors to the console for debugging
    return render(request, 'reservation_form.html', context)


def reservation_success(request):
    return render(request, 'reservation_success.html')


def menu(request):
    data = Menu.objects.all()
    menu_data = {'menu' : data}
    
    return render(request,'menu.html', menu_data)

def menu_item(request,pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
        return render(request, 'menu_item.html', {'menu_item': menu_item} )

