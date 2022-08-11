from __future__ import annotations

from datetime import datetime
from typing import Optional

from django.http import HttpRequest, HttpResponse
from django.http.request import QueryDict
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods
from django.views import View

from todo.models import TodoItem


class TodoIndex(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        items = TodoItem.objects.all()
        return render(request, "index.html", context={"items": items})

    def post(self, request: HttpRequest) -> HttpResponse:
        print("post", request.POST)
        TodoItem.objects.create(description=request.POST['description'])
        items = TodoItem.objects.all()
        return render(request, "todo-list.html", context={"items": items})

    def put(self, request: HttpRequest) -> HttpResponse:
        data = QueryDict(request.body)
        print("put", data, data.get("done"))
        params = {}
        if data.get("done"):
            params["done_at"] = datetime.utcnow()
        if data.get("description"):
            params["description"] = data["description"]
        TodoItem.objects.filter(pk=data["id"]).update(**params)
        items = TodoItem.objects.all()
        return render(request, "todo-list.html", context={"items": items})
