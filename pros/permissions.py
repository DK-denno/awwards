from rest_framework.permissions import SAFEMETHODS,BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.methos in SAFEMETHODS:
            return True
        return request.user.is_staff
        