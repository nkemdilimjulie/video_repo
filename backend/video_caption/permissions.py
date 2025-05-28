from rest_framework import permissions

class CanAddCaptions(permissions.BasePermission):
    """
    Custom permission to allow only authenticated users to add captions to videos.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user  # Ensure user owns the video


#mmmmmmmmmmmmm  Generalized Permission Class
# from rest_framework import permissions

# class IsOwnerOrAdmin(permissions.BasePermission):
#     """
#     Custom permission to allow users to manage their own videos,
#     while allowing admins full access.
#     """

#     def has_permission(self, request, view):
#         # Allow access if user is authenticated
#         return request.user and request.user.is_authenticated

#     def has_object_permission(self, request, view, obj):
#         # Allow if user is an admin or if the user owns the object
#         return request.user.is_staff or obj.user == request.user
