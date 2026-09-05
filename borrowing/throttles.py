from rest_framework.throttling import UserRateThrottle

class CustomerUserThrottle(UserRateThrottle):

    rate="3/minute"


    def allow_request(self, request, view):
        if request.user.is_staff:
            return True
        return super().allow_request(request, view)
    
