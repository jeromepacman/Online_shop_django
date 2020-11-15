from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="prénom")
    last_name = models.CharField(max_length=50, verbose_name="nom")
    email = models.EmailField()
    address = models.CharField(max_length=250, verbose_name="adresse")
    postal_code = models.CharField(max_length=5,verbose_name="code postal")
    city = models.CharField(max_length=100, verbose_name="ville")
    created = models.DateTimeField(auto_now_add=True, verbose_name="date de création")
    updated = models.DateTimeField(auto_now=True, verbose_name="date de mise à jour")
    paid = models.BooleanField(default=False, verbose_name="validation")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Commande'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name="historique")
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name="produit")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="prix")
    quantity = models.PositiveIntegerField(default=1, verbose_name="quantité")

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity



