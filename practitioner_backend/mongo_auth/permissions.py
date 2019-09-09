from rest_framework import permissions
from mongo_auth.utils import login_status


class AuthenticatedOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            flag, user_obj = login_status(request)
            print(flag)
            print(user_obj)
            request.user = None
            if flag:
                request.user = user_obj
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

class AuthenticatedOnlyAndMyUserOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        print("Paso Check")
        #obj = self.get_object()
        return True;

    def has_object_permission(self, request, view, obj):
        print("Hello")
        #obj = get_object_or_404(self.get_queryset(), email=self.kwargs["email"])
        print(obj)
        return True
