def middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print("test middleware")
        response = get_response(request)
        print("test middleware", response)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
