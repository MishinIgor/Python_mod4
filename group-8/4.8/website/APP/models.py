from django.db import models
#models.py
class Catalog(models.Model):
    brand = models.CharField(max_length=100,verbose_name='Название')
    description = models.TextField(blank=True)
    #blank=True позволяет сделать поле необязательным
    #для заполнения
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    title = models.CharField(max_length=30, default='Введите название товара', 
                             verbose_name='название товара', 
                             unique=True)
    brand = models.ForeignKey(Catalog,on_delete=models.CASCADE,
                              default=1, verbose_name='Производитель')
    price = models.IntegerField(default=0, verbose_name='Цена')
    amount = models.IntegerField(default=0, verbose_name='Товара на складе')
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    def __str__(self):
        return f'{self.title} {self.brand}'
    
    
    
    
