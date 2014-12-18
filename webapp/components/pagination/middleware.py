class PaginationMiddleware(object):
    """
    Inserts a variable representing the current page onto the request object if
    it exists in either **GET** or **POST** portions of the request.
    """
    def process_request(self, request):
        if "market/edit/" in request.path and "/photos/" in request.path:
            request.page = int(request.GET.get("page",request.session.get("ap_page", 1)))
        else:
            try:
                request.page = int(request.REQUEST['page'])
            except (KeyError, ValueError, TypeError):
                request.page = 1