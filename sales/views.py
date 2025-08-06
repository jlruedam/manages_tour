from django.shortcuts import render, get_object_or_404, redirect
from .models import Agency, Tour, Client, Employee, Sale, Role, Referrer, Payment, Provider
from .forms import AgencyForm, TourForm, ClientForm, SaleForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import Group 
from django.db.models import Sum
import json


def home(request):
    tours = Tour.objects.all()
    ctx = {
        'view_home': True,
        'tours':tours
    }
    return render(request, 'home/index.html',ctx)

# ========== MENU ==========
def menu(request):
    return render(request, 'home/menu.html')

# ========== SALE ==========
def sale_list(request):
    sales = Sale.objects.select_related('tour', 'client', 'employee', 'referrer').all()
    sales = sales.annotate(
        total_payments=Sum('payments__value')
    )
    tours = Tour.objects.all()
    clients = Client.objects.all()
    referrers = Referrer.objects.all()

    vendors = Employee.objects.filter(rol = 1)
    ctx = {
        'view_sale_list':True,
        'sales': sales,
        'tours':tours,
        'clients':clients,
        'vendors': vendors,
        'referrers':referrers
    }
    return render(request, 'sales/sale_list.html', ctx)

def create_sale(request):
    if request.method == 'POST':

        response = request.POST

        payments_json = request.POST.get('payments', '[]')
        payments_data = json.loads(payments_json)

        print("ABONOS: ",payments_data)


        tour = Tour.objects.get(name_tour = response.get('tour'))

        client = str(response.get('client')).split("-")
        client = Client.objects.get(num_doc  = client[0])

        closer = str(response.get('closer')).split("-")
        closer = Employee.objects.get(num_doc = closer[0])

        referrer = str(response.get('referrer')).split("-")
        referrer = Referrer.objects.get(num_doc = referrer[0])

        value = float(response.get('value'))
        quantity = int(response.get('quantity'))
        notes = response.get('notes')

        print(tour, client, closer,referrer, value, quantity, notes)

        new_sale = Sale(
            tour = tour,
            client = client,
            employee = closer,
            referrer = referrer,
            value_sale_unit = value,
            quantity = quantity,
            total_sale = quantity*value,
            observations = notes
        )
        new_sale.save()

        for payment in payments_data:
            Payment.objects.create(
                sale=new_sale,  # la venta creada
                options_payment=payment['options_payment'],
                bank_platform=payment['options_bank'],
                value=float(payment['value']),
                # payment_date=payment['payment_date'],
                payment_reference=payment['payment_reference'],
                # confirmed=payment['confirmed'],
                note=payment['note'],
                # document_url=payment['document_url']
            )
        
        
        return JsonResponse({
            'success': True,
            'message': 'Venta creada correctamente.',
            'sale': {
                'num_doc': client.num_doc,
                'name': client.name,
                'sale': new_sale.id,
                'tour':tour.name_tour,
                'total_sale':new_sale.total_sale
            }
        })
    return JsonResponse({'success': False, 'message': 'Método no permitido'})

def sale_detail_view(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    tour = sale.tour
    images = tour.images.all()
    payments = sale.payments.all()

    total_abonado = sum(p.value for p in payments)
    saldo_pendiente = sale.total_sale - total_abonado

    context = {
        'sale': sale,
        'tour': tour,
        'images': images,
        'payments': payments,
        'total_abonado': total_abonado,
        'saldo_pendiente': saldo_pendiente,
    }
    return render(request, 'sales/sale_detail.html', context)

# def sale_update(request, pk):
#     sale = get_object_or_404(Sale, pk=pk)
#     form = SaleForm(request.POST or None, instance=sale)
#     if form.is_valid():
#         form.save()
#         messages.success(request, "Venta actualizada.")
#         return redirect('sale_list')
#     return render(request, 'sales/sale_form.html', {'form': form})

# def sale_delete(request, pk):
#     sale = get_object_or_404(Sale, pk=pk)
#     sale.delete()
#     messages.success(request, "Venta eliminada.")
#     return redirect('sale_list')


# ========== AGENCY ==========
def agency_list(request):
    agencies = Agency.objects.all()
    return render(request, 'agencies/agency_list.html', {'agencies': agencies})

# ========== TOUR ==========
def tour(request,id):
    print("ID TOUR: ", id)
    tour = get_object_or_404(Tour, pk=id)
    return render(request, 'tours/tour.html', {'tour':tour})

def tour_list(request):
    agencies = Agency.objects.all()
    providers = Provider.objects.all()
    tours = Tour.objects.select_related('agency', 'provider').prefetch_related('images').all()
    ctx ={
        'tours': tours,
        'agencies':agencies,
        'providers':providers
    }
    return render(request, 'tours/tours_list.html', ctx)

def tour_create(request):
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Tour creado correctamente.")
            return redirect('tour_list')
        else:
            messages.error(request, "Hubo un error al crear el tour. Verifica los datos.")
    else:
        form = TourForm()

    return render(request, 'tours/tour_list.html', {'form': form})

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




def referrer_create(request):
    if request.method == "POST":
        type_doc = request.POST.get("type_doc")
        num_doc = request.POST.get("num_doc")
        name = request.POST.get("name")
        tel = request.POST.get("tel")

        if Referrer.objects.filter(num_doc=num_doc).exists():
            return JsonResponse({'success': False, 'message': 'Ya existe un jalador con ese número de documento.'})

        referrer = Referrer.objects.create(
            type_doc=type_doc,
            num_doc=num_doc,
            name=name,
            tel=tel
        )

        return JsonResponse({
            'success': True,
            'referrer': {
                'num_doc': referrer.num_doc,
                'name': referrer.name
            }
        })

    return JsonResponse({'success': False, 'message': 'Petición inválida'})


def payment_create(request):
    pass
    # if request.method == 'POST':
    #     form = ClientForm(request.POST)
    #     if form.is_valid():
    #         client = form.save()
    #         return JsonResponse({
    #             'success': True,
    #             'message': 'Cliente creado correctamente.',
    #             'client': {
    #                 'num_doc': client.num_doc,
    #                 'name': client.name
    #             }
    #         })
    #     else:
    #         return JsonResponse({'success': False, 'message': 'Datos inválidos', 'errors': form.errors})
    # return JsonResponse({'success': False, 'message': 'Método no permitido'})