from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.constraints import UniqueConstraint


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "상품 분류"


class Product(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "정상"
        SOLD_OUT = "sold_out", "품절"
        OBSOLETE = "obsolete", "단종"
        INACTIVE = "inactive", "비활성화"

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_constraint=False
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    status = models.CharField(
        choices=Status.choices, default=Status.INACTIVE, max_length=10
    )
    photo = models.ImageField(blank=True, upload_to="mall/product/%Y/%m/%d")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<{self.pk}> {self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "상품"
        ordering = ["-id"]


class CartProduct(models.Model):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        db_constraint=False,
        related_name="cart_product_set",
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_constraint=False)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"<{self.pk}> {self.product.name} - {self.quantity}"

    class Meta:
        verbose_name = verbose_name_plural = "장바구니 상품"
        constraints = [
            UniqueConstraint(fields=["user", "product"], name="unique_cart_product")
        ]
