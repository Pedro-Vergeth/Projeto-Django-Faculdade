from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from .models import Manager, Representante  

class MultiModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Manager.objects.get(email=username)
            if user.check_password(password):
                return user
        except Manager.DoesNotExist:
            pass

        try:
            user = Representante.objects.get(email=username)
            if user.check_password(password):
                return user
        except Representante.DoesNotExist:
            return None

        return None

    def get_user(self, user_id):
        try:
            return Manager.objects.get(pk=user_id)
        except Manager.DoesNotExist:
            try:
                return Representante.objects.get(pk=user_id)
            except Representante.DoesNotExist:
                return None
