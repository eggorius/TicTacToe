from django.http import HttpResponse


def game_is_available(view_func):
    def wrapper_func(request, name, *args, **kwargs):
        if request.user.groups.exists():
            group = request.user.groups.all()[0]
            if group.name == 'blocked':
                return HttpResponse('UPS! You are blocked!<br> <a href=\"/login\">Log in</a>')
        return view_func(request, name, *args, **kwargs)
    return wrapper_func
