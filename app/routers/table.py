from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from ..internal.common import templates, VERSION, GIT_COMMIT

router = APIRouter(prefix="/table")


class ItemStore:
    """In-memory item store used to demo the table UI without a database."""

    CATEGORIES = ["Hardware", "Software", "Service"]

    def __init__(self):
        # Each item is [name, category, value, description]
        self.items = [
            ["Laptop", "Hardware", 1200, "Developer workstation"],
            ["License", "Software", 99, "Annual editor license"],
            ["Support", "Service", 500, "Priority support plan"],
        ]

    def list_categories(self):
        return self.CATEGORIES

    def list_items(self):
        return sorted(self.items, key=lambda row: row[0])

    def add_item(self, name, category, value, description):
        if any(row[0] == name for row in self.items):
            raise RuntimeError("An item with the same name already exists.")
        self.items.append([name, category, value, description])

    def edit_item(self, name, category, value, description):
        for row in self.items:
            if row[0] == name:
                row[1], row[2], row[3] = category, value, description
                break

    def delete_item(self, name):
        self.items = [row for row in self.items if row[0] != name]


store = ItemStore()


@router.get("", response_class=HTMLResponse)
async def get_table_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="table.html",
        context={
            "data_source": store.list_items(),
            "categories": store.list_categories(),
            "version": VERSION,
            "git_commit": GIT_COMMIT,
        },
    )


class AddItemRequest(BaseModel):
    name: str
    category: str
    value: int
    description: str


@router.post("/add_item", response_class=HTMLResponse)
async def add_item(request: Request, item: AddItemRequest):
    store.add_item(item.name, item.category, item.value, item.description)
    return templates.TemplateResponse(
        name="table.html",
        context={
            "request": request,
            "data_source": store.list_items(),
            "categories": store.list_categories(),
            "version": VERSION,
            "git_commit": GIT_COMMIT,
        },
    )


class EditItemRequest(BaseModel):
    name: str
    category: str
    value: int
    description: str


@router.post("/edit_item", response_class=HTMLResponse)
async def edit_item(request: Request, item: EditItemRequest):
    store.edit_item(item.name, item.category, item.value, item.description)
    return templates.TemplateResponse(
        name="table.html",
        context={
            "request": request,
            "data_source": store.list_items(),
            "categories": store.list_categories(),
            "version": VERSION,
            "git_commit": GIT_COMMIT,
        },
    )


class DeleteItemRequest(BaseModel):
    name: str


@router.post("/delete_item", response_class=HTMLResponse)
async def delete_item(request: Request, item: DeleteItemRequest):
    store.delete_item(item.name)
    return templates.TemplateResponse(
        name="table.html",
        context={
            "request": request,
            "data_source": store.list_items(),
            "categories": store.list_categories(),
            "version": VERSION,
            "git_commit": GIT_COMMIT,
        },
    )
