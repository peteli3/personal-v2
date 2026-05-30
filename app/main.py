from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .internal.common import templates, VERSION, GIT_COMMIT
from .routers.table import router as table_router
from .routers.counter import router as counter_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(table_router)
app.include_router(counter_router)


@app.get("/version")
def get_version():
    return {
        "version": VERSION,
        "git_commit": GIT_COMMIT,
    }


@app.get("/", response_class=HTMLResponse)
def get_home_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "version": VERSION,
            "git_commit": GIT_COMMIT,
        },
    )
