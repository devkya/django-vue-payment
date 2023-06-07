from django.conf import settings
from django.db import models
from uuid import uuid4
from django.core.validators import MinValueValidator
from django.http import Http404
from iamport import Iamport
import logging

logger = logging.getLogger("portone")


# Create your models here.
class Payment(models.Model):
    class StatusCoices(models.TextChoices):
        READY = "ready", "미결제"
        PAID = "paid", "결제완료"
        CANCELLED = "cancelled", "결제취소"
        FAILED = "failed", "결제실패"

    uid = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(
        validators=[MinValueValidator(1, message="1 이상의 숫자를 입력해주세요.")]
    )
    # ready, paid, cancelled, failed
    status = models.CharField(
        max_length=10,
        default=StatusCoices.READY,
        choices=StatusCoices.choices,
        db_index=True,
    )
    is_paid_ok = models.BooleanField(default=False, editable=False, db_index=True)

    @property
    def merchant_uid(self) -> str:
        print(self.uid.hex)
        return self.uid.hex

    def portone_check(self, commit=True):
        api = Iamport(
            imp_key=settings.PORTONE_API_KEY, imp_secret=settings.PORTONE_API_SECRET
        )
        try:
            meta = api.find(merchant_uid=self.merchant_uid)
        except (Iamport.ResponseError, Iamport.HttpError) as e:
            logger.error(str(e), exc_info=e)
            raise Http404(str(e))

        self.status = meta["status"]
        self.is_paid_ok = meta["status"] == "paid" and meta["amount"] == self.amount
        if commit:
            self.save()
        return meta
