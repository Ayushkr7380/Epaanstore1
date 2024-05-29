from django.shortcuts import redirect

# Decorators kind of middlewares

#Authentications
def auth1(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        return view_function(request,*args,**kwargs)
    return wrapped_view

#Loggedin users
def loggedin1(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_function(request,*args,**kwargs)
    return wrapped_view

#Prevent Direct Access
def prevent_direct_access(view_function):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Check if the user came from a referrer
            if 'HTTP_REFERER' in request.META:
                # Check if the referrer is from the same domain
                referrer = request.META['HTTP_REFERER']
                if request.build_absolute_uri('/') in referrer:
                    return view_function(request, *args, **kwargs)
            # If not, redirect to a safe page
            return redirect('home')
        # If user is not authenticated, redirect to login page
        return redirect('login')
    return wrapped_view