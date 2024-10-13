from rest_framework.permissions import BasePermission

class IsAdministrator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ["administrator"]

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ["staff","administrator"]
    
class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ["teacher","administrator","staff"]
   
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        print("jwt value = ",request.user.is_authenticated)
        print("role = ",request.user.role)
        return request.user.is_authenticated and request.user.role in ["student","administrator","staff","teacher"] 

