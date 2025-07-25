from django.db import models
from django.utils.timezone import now


class Agency(models.Model):
    nit = models.CharField(max_length=10)
    name_agency = models.CharField(max_length=100)
    email_agency = models.EmailField(max_length=100)
    tel_agency = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.nit}: {self.name_agency}"


class Referrer(models.Model):
    type_doc = models.CharField(max_length=10)
    num_doc = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    client_data = models.CharField(max_length=200)
    bank = models.CharField(max_length=100)
    type_count = models.CharField(max_length=100)
    num_count = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.num_doc}: {self.name}"


class Provider(models.Model):
    nit = models.CharField(max_length=10)
    name_provider = models.CharField(max_length=100)
    email_provider = models.EmailField(max_length=100)
    tel_provider = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.nit}: {self.name_provider}"


class Tour(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='tours')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='tours')
    name_tour = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price_sale = models.FloatField()
    price_total = models.FloatField()
    image_path = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name_tour


class Client(models.Model):
    tipo_doc = models.CharField(max_length=100)
    num_doc = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    tel = models.CharField(max_length=200, blank=True, null=True)
    hotel = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.num_doc}: {self.name}"


class Vendor(models.Model):
    type_doc = models.CharField(max_length=10)
    num_doc = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.num_doc}: {self.name}"


class Sale(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='sales')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sales')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='sales')
    referrer = models.ForeignKey(Referrer, on_delete=models.CASCADE, related_name='sales')
    value_sale_unit = models.FloatField()
    quantity = models.IntegerField()
    total_sale = models.FloatField()
    observations = models.CharField(max_length=250, default='')
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Sale {self.id}: Tour {self.tour_id}, Client {self.client_id}"


class Payment(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='payments')
    options_payment = models.CharField(max_length=100)
    value = models.FloatField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)


class Commission(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='commissions')
    type = models.CharField(max_length=100)
    beneficiary_num = models.CharField(max_length=100)
    beneficiary_name = models.CharField(max_length=100)
    percentage = models.FloatField()
    value_sale = models.FloatField()
    value_commission = models.FloatField()
    observations = models.CharField(max_length=250, default='')
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)


