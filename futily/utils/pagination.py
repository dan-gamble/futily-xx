from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def __init__(self):
        super(CustomPagination, self).__init__()

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'prev': self.get_previous_link(),
            'current': self.page.number,
            'total': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            'results': data
        })
