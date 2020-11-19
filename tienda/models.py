from django.db import models

class categories (models.Model):
  #idCategory = models.AutoField( primary_key = True)
  nameCategory = models.CharField( max_length = 50, unique = True )
def __str__(self):
            return self.nameCategory

class customers (models.Model):
  #idCustomer=models.AutoField( primary_key = True)
  nameCustomer=models.CharField( max_length = 50)
  address=models.CharField( max_length = 100)
  emailCustomer=models.CharField( max_length = 100)
  phoneCustomer=models.CharField( max_length = 10)
  def __str__(self):
            return self.nameCustomer
class products (models.Model):
  #idProduct=models.AutoField( primary_key = True)
  nameProduct=models.CharField(max_length=50)
  price=models.FloatField()
  stok=models.IntegerField()
  discontinued=models.BooleanField()
  #Categories
  idCategory=models.ForeignKey(categories,on_delete=models.CASCADE)
  def __str__(self):
            return self.nameProduct
class order (models.Model):
  #idOrder=models.AutoField(primary_key=True)
  dataOrder=models.DateTimeField()
  shippedDate=models.DateTimeField()
  #Customer
  idCustomer=models.ForeignKey(customers,on_delete=models.CASCADE)
  def __str__(self):
            return self.dataOrder

class orderDetail(models.Model):
    #idDetail=models.AutoField(primary_key=True)
    price=models.FloatField()
    discount=models.FloatField()
    quantity=models.FloatField()
    #fkOrder
    idOrder=models.ForeignKey(order,on_delete=models.CASCADE)
    #fkProduct
    idProduct=models.ForeignKey(products,on_delete=models.CASCADE)
    def __str__(self):
            return self.price