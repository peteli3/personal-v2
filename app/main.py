from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .internal.common import templates, VERSION, GIT_COMMIT
from .internal import profile

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


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
            "name": profile.NAME,
            "tagline": profile.TAGLINE,
            "profile_image": profile.PROFILE_IMAGE,
            "resume_url": profile.RESUME_URL,
            "link_groups": profile.LINK_GROUPS,
        },
    )
