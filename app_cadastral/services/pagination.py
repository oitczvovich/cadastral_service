from fastapi import Request
from starlette import routing


class Pagination:
    def __init__(self, request: Request, total_count: int, page: int, size: int):
        self.request = request
        self.total_count = total_count
        self.page = page
        self.size = size

    def get_next_page(self):
        end_index = self.page * self.size
        next_page = self.page + 1 if end_index < self.total_count else None
        return next_page

    def get_prev_page(self):
        prev_page = self.page - 1 if self.page > 1 else None
        return prev_page

    def get_next_url(self):
        next_page = self.get_next_page()
        if next_page is not None:
            url = routing.URL(scope=self.request.scope)
            next_url = str(url.include_query_params(page=next_page))
            return next_url

    def get_prev_url(self):
        prev_page = self.get_prev_page()
        if prev_page is not None:
            url = routing.URL(scope=self.request.scope)
            prev_url = str(url.include_query_params(page=prev_page))
            return prev_url
