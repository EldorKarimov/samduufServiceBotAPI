from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

class RequestedUser(BaseModel):
    class Meta:
        verbose_name = _("requested user")
        verbose_name_plural = _("requested users")
    REQUESTED_USER_TYPE = (
        ('STUDENT', _("Student")),
        ('EMPLOYEE', _("Employee"))
    )
    telegram_id = models.CharField(_("telegram id"), max_length=20, unique=True)
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    group = models.CharField(_("group"), max_length=150, null=True)
    type = models.CharField(_("type"), max_length=8, choices=REQUESTED_USER_TYPE)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class RequestedUserMessage(BaseModel):
    REQUEST_TYPE = (
        (1, _("Get a login password for the Internet")),
        (2, _("Kerio login password recovery")),
    )
    requested_user = models.ForeignKey(RequestedUser, on_delete=models.CASCADE, verbose_name=_("requested user"))
    message = models.TextField(_("xabar"), null=True, blank=True)
    request_type = models.IntegerField(_("request type"), choices=REQUEST_TYPE)

    def __str__(self):
        return f"{self.requested_user.get_full_name}-{self.request_type}"