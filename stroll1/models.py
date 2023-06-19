from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    review = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)  

class Destination(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300) 
    price = models.FloatField()
    img = models.ImageField(upload_to="pics")

    def __str__(self):
        return self.name
    
    @property 
    def imageUrl(self):
        try:
            url = self.img.url
        
        except:
            url = ''
        return url
    

class Custom(models.Model):
    destnation = models.CharField(max_length=100,null=True)
    activity = models.CharField(max_length=100, null=True)
    duration = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Blogs(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=5000,null=True)
    price = models.CharField(max_length=100, null=True)
    img = models.ImageField(upload_to="pics")
    iframe = models.CharField(max_length=500, null=True)
    tag = models.CharField(max_length=500, null=True, blank=True)

    @property 
    def ImageUrl(self):
        try:
            url = self.img.url

        except:
            url = ''
            
        return url

    def __str__(self):
        return self.name
    


class Rating(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name= 'rating')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(choices=((1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')))
    likes = models.PositiveIntegerField(default=0)
    unlikes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('destination', 'user')

    def __str__(self):
        return f"{self.user}'s {self.rating}-star rating for {self.destination}"
    
class product(models.Model):
        name = models.CharField(max_length = 200, null=True, blank=True)
        price = models.FloatField(max_length = 200, null=True, blank=True)
        image = models.ImageField(null=True, blank=True)
        featured = models.BooleanField(default=False, null=True, blank=True )

        def __str__(self):
            return self.name

        @property
        def imageURL(self):
            try:
                url= self.image.url
            except:
                url = ''
            return url
    
# class Order(models.Model):
#         name = models.CharField(max_length = 200, null=True)
#         quantity = models.CharField(max_length = 200, null=True)
#         date_ordered = models.DateTimeField(auto_now_add=True, null=True)
#         product = models.ManyToManyField(product)
#         customer = models.ForeignKey(Customer, on_delete= models.CASCADE, blank=True, null=True) 
#         complete = models.BooleanField(default=False, null=True, blank=True )
#         transaction_id = models.CharField(max_length = 200, null=True)
    
        # @property
        # def get_cart_total(self):
        #     orderitems = self.orderitem_set.all()
        #     total = sum(orderitem.get_total for orderitem in orderitems)
        #     return total
            
        # @property
        # def get_cart_items_number(self):
        #     orderitems = self.orderitem_set.all()
        #     total = sum(orderitem.quantity for orderitem in orderitems)
        #     return total


class Order(models.Model):
    name = models.CharField(max_length = 200, null=True)
    quantity = models.CharField(max_length = 200, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    product = models.ManyToManyField(product)
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, blank=True, null=True) 
    complete = models.BooleanField(default=False, null=True, blank=True )
    transaction_id = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return str(self.name)
    
    # @property
    # def shipping(self):
    #     shipping = False
    #     orderitems = self.orderitem_set.all()
    #     for orderitem in orderitems:
    #         if orderitem.product.digital == False:
    #             shipping=True
       
    #     return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum(orderitem.get_total for orderitem in orderitems)
        return total
        
    @property
    def get_cart_items_number(self):
        orderitems = self.orderitem_set.all()
        total = sum(orderitem.quantity for orderitem in orderitems)
        return total
    
class OrderItem(models.Model):
        product = models.ForeignKey(product, on_delete=models.CASCADE, null=True, blank=True)
        order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
        quantity = models.IntegerField(default=0, null=True, blank=True)
        date_added = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.product.name

        @property
        def get_total(self):
            total = self.quantity * self.product.price
            return total
                                         