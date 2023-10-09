from django.contrib.auth.models import User
from django.db import models
from book.models import Allbooks

class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Allbooks, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    auther = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='book/images/', null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)






