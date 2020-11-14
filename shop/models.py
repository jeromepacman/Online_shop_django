from django.db import models

from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name="nom")
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="categorie")
    name = models.CharField(max_length=150, db_index=True, verbose_name="nom")
    slug = models.SlugField(max_length=150, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="prix")
    available = models.BooleanField(default=True, verbose_name="disponibilité")
    created = models.DateTimeField(auto_now_add=True, verbose_name="date de création")
    updated = models.DateTimeField(auto_now=True, verbose_name="date de mise à jour")

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'produit'
        verbose_name_plural = 'produits'

    def __str__(self): return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
