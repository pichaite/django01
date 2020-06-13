from django.db import models

from django.urls import reverse

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255,unique=True)
	slug = models.SlugField(max_length=255,unique=True)


	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name = 'หมวดหมู่สินค้า'
		verbose_name_plural = "ข้อมูประเภทสินค้า"

	def get_url(self):
		return reverse('product_by_category',args=[self.slug])


class Product(models.Model):
	name = models.CharField(max_length=255,unique=True)
	slug = models.SlugField(max_length=255,unique=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	Category = models.ForeignKey(Category,on_delete=models.CASCADE)
	image = models.ImageField(upload_to="product",blank=True) 
	stock = models.IntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name = 'สินค้า'
		verbose_name_plural = "ข้อมูลสินค้า"

	def get_url(self):
		return reverse('productDetail',args=[self.Category.slug,self.slug])


class Cart(models.Model):
	cart_id = models.CharField(max_length=255,blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.cart_id

	class Meta:
		ordering = ('date_added',)
		db_table = 'cart'
		verbose_name = 'ตะกร้าสินค้า'
		verbose_name_plural = "ข้อมูลตะกร้าสินค้า"

class CartItem(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
	quantity = models.IntegerField()
	active = models.BooleanField(default=True)

	def sub_total(self):
		return self.product.price * self.quantity

	def __str__(self):
		return self.product.name

	class Meta:
		db_table = 'cartItem'
		verbose_name = 'รายการสินค้าในตะกร้า'
		verbose_name_plural = "ข้อมูลรายการสินค้าในตะกร้าสินค้า"


