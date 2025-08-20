from __future__ import annotations

from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from docsearch.core.config import get_settings
from docsearch.core.logging import setup_logging
from docsearch.db.init import init_db
from docsearch.db.session import engine
from docsearch.services.search import search_pages


BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "web" / "templates"
STATIC_DIR = BASE_DIR / "web" / "static"


def create_app() -> FastAPI:
    settings = get_settings()
    setup_logging(settings.debug)

    app = FastAPI(title=settings.app_name)

    # Шаблоны и статика
    templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

    @app.on_event("startup")
    def _startup() -> None:
        # Инициализируем БД и FTS5 при старте
        init_db(engine)

    @app.get("/healthz", response_class=JSONResponse)
    async def healthz() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/", response_class=HTMLResponse)
    async def index(request: Request) -> HTMLResponse:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "app_name": settings.app_name},
        )

    @app.get("/api/search", response_class=JSONResponse)
    async def api_search(q: str = "", k: int = 20) -> JSONResponse:
        results = search_pages(q, limit=max(1, min(k, 100)))
        return JSONResponse({"query": q, "count": len(results), "results": results})

    return app


app = create_app()
