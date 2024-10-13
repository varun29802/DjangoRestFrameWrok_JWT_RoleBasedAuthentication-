from rest_framework.permissions import BasePermission

# This for specific role if admin then admin can access admin api's only
# Staff can access Staff Api's only
# Teacher can access Teacher Api's only
# Student can access Student Api's only

class isAdministrator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "administrator"

class isTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "teacher"

class isStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "studnet"

class isStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "staff"
    

# This is a type of 
# admin can access all 
# staff can access Staff, Teacher, Student 
# Teacher can access Teacher, Studnet 
# Studnet can access Student


# class isAdministrator(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role in ["administrator"]

# class isStaff(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role in ["staff","administrator"]
    
# class isTeacher(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role in ["teacher","administrator","staff"]

# class isStudent(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role in ["student","administrator","staff","teacher"]
