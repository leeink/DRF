from rest_framework.pagination import LimitOffsetPagination

class LargeResultsSetPagination(LimitOffsetPagination):
    default_limit = 500
    limit_query_param = 'limit'
    offset_query_param = 'offset'

class StandardResultsSetPagination(LimitOffsetPagination):
    default_limit = 200
    limit_query_param = 'limit'
    offset_query_param = 'offset'