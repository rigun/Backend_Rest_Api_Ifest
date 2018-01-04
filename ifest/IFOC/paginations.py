from rest_framework.pagination import (
    PageNumberPagination,
)

class dataPageNumberPagination(PageNumberPagination):
    page_size = 4