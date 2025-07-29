from django.shortcuts import render, get_object_or_404, redirect
from .models import Agency, Tour, Client, Employee, Sale, Role
from .forms import AgencyForm, TourForm, ClientForm, SaleForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import Group 


# ========== MENU ==========
def menu(request):
    return render(request, 'home/menu.html')


# ========== AGENCY ==========
def agency_list(request):
    agencies = Agency.objects.all()
    return render(request, 'agencies/agency_list.html', {'agencies': agencies})

def agency_create(request):
    if request.method == 'POST':
        form = AgencyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Agencia creada correctamente.")
            return redirect('agency_list')
    else:
        form = AgencyForm()
    return render(request, 'agencies/agency_form.html', {'form': form})

def agency_update(request, pk):
    agency = get_object_or_404(Agency, pk=pk)
    form = AgencyForm(request.POST or None, instance=agency)
    if form.is_valid():
        form.save()
        messages.success(request, "Agencia actualizada.")
        return redirect('agency_list')
    return render(request, 'agencies/agency_form.html', {'form': form})

def agency_delete(request, pk):
    agency = get_object_or_404(Agency, pk=pk)
    agency.delete()
    messages.success(request, "Agencia eliminada.")
    return redirect('agency_list')


# ========== TOUR ==========
def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'tours/tour_list.html', {'tours': tours})

def tour_create(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tour creado correctamente.")
            return redirect('tour_list')
    else:
        form = TourForm()
    return render(request, 'tours/tour_form.html', {'form': form})

def tour_update(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    form = TourForm(request.POST or None, instance=tour)
    if form.is_valid():
        form.save()
        messages.success(request, "Tour actualizado.")
        return redirect('tour_list')
    return render(request, 'tours/tour_form.html', {'form': form})

def tour_delete(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    tour.delete()
    messages.success(request, "Tour eliminado.")
    return redirect('tour_list')


# ========== CLIENT ==========
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return JsonResponse({
                'success': True,
                'message': 'Cliente creado correctamente.',
                'client': {
                    'num_doc': client.num_doc,
                    'name': client.name
                }
            })
        else:
            return JsonResponse({'success': False, 'message': 'Datos inválidos', 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Método no permitido'})

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        messages.success(request, "Cliente actualizado.")
        return redirect('client_list')
    return render(request, 'clients/client_form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    messages.success(request, "Cliente eliminado.")
    return redirect('client_list')

# ========== VENDOR ==========
# def vendor_list(request):
#     vendors = Vendor.objects.all()
#     return render(request, 'vendors/vendor_list.html', {'vendors': vendors})

# def vendor_create(request):
#     if request.method == 'POST':
#         form = VendorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Vendedor creado.")
#             return redirect('vendor_list')
#     else:
#         form = VendorForm()
#     return render(request, 'vendors/vendor_form.html', {'form': form})

# def vendor_update(request, pk):
#     vendor = get_object_or_404(Vendor, pk=pk)
#     form = VendorForm(request.POST or None, instance=vendor)
#     if form.is_valid():
#         form.save()
#         messages.success(request, "Vendedor actualizado.")
#         return redirect('vendor_list')
#     return render(request, 'vendors/vendor_form.html', {'form': form})

# def vendor_delete(request, pk):
#     vendor = get_object_or_404(Vendor, pk=pk)
#     vendor.delete()
#     messages.success(request, "Vendedor eliminado.")
#     return redirect('vendor_list')


# ========== SALE ==========
def sale_list(request):
    sales = Sale.objects.select_related('tour', 'client', 'employee', 'referrer').all()
    tours = Tour.objects.all()
    clients = Client.objects.all()

    vendors = Employee.objects.filter(rol = 1)
    ctx = {
        'sales': sales,
        'tours':tours,
        'clients':clients,
        'vendors': vendors
    }
    return render(request, 'sales/sale_list.html', ctx)

# def sale_create(request):
#     if request.method == 'POST':
#         form = SaleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Venta registrada.")
#             return redirect('sale_list')
#     else:
#         form = SaleForm()
#     return render(request, 'sales/sale_form.html', {'form': form})

# def create_sale(request):
#     if request.method == 'POST':
#         form = SaleForm(request.POST)
#         if form.is_valid():
#             sale = form.save(commit=False)
#             # Calculamos el total antes de guardar, si se desea
#             sale.total_sale = sale.value_sale_unit * sale.quantity
#             # sale.created_at = now()
#             # sale.updated_at = now()
#             sale.save()
#             return redirect('sale_success')  # Redirige a una vista de éxito
#     else:
#         form = SaleForm()

#     return render(request, 'sales/create-sale.html', {'form': form})
@require_POST
def create_sale(request):
    form = SaleForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)


def sale_update(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    form = SaleForm(request.POST or None, instance=sale)
    if form.is_valid():
        form.save()
        messages.success(request, "Venta actualizada.")
        return redirect('sale_list')
    return render(request, 'sales/sale_form.html', {'form': form})

def sale_delete(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    sale.delete()
    messages.success(request, "Venta eliminada.")
    return redirect('sale_list')
