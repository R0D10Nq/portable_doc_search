from __future__ import annotations

import typer
import uvicorn

from docsearch.core.config import get_settings
from docsearch.db.init import init_db
from docsearch.db.session import engine

app = typer.Typer(help="Portable DocSearch CLI")


@app.command()
def init_db_cmd() -> None:
    """Инициализировать базу данных и объекты FTS5."""
    init_db(engine)
    typer.echo(f"База данных инициализирована: {get_settings().database_url}")


@app.command()
def run(host: str | None = None, port: int | None = None, reload: bool = True) -> None:
    """Запустить локальный сервер Uvicorn."""
    settings = get_settings()
    uvicorn.run(
        "docsearch.main:app",
        host=host or settings.host,
        port=port or settings.port,
        reload=reload,
    )


@app.command()
def version() -> None:
    from docsearch import __version__

    typer.echo(__version__)


if __name__ == "__main__":
    app()
