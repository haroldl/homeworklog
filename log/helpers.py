
def cookie_value(request, cookie_name, default_value):
    if cookie_name in request.COOKIES:
        return request.COOKIES[cookie_name]
    else:
        return default_value
