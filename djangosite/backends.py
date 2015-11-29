from supermarket.models import Employee

class ModelBackend():
    def authentication(self, username=None, password=None):
        if username:
            try:
                user = Employee.objects.get(username=username)
                if user.check_password(password):
                    return user
            except user.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return Employee.objects.get(pk=user_id)
        except Employee.DoesNotExist:
            return None
