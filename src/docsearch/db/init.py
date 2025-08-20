from __future__ import annotations

from sqlalchemy import text
from sqlalchemy.engine import Engine

from .models import Base


def init_db(engine: Engine) -> None:
    """Создаёт базовые таблицы и объекты FTS5 (если их ещё нет)."""
    # Создаём обычные таблицы
    Base.metadata.create_all(bind=engine)

    with engine.connect() as conn:
        # Включаем внешний ключ в SQLite
        conn.exec_driver_sql("PRAGMA foreign_keys=ON;")

        # Создаём виртуальную таблицу FTS5 для pages.text
        conn.exec_driver_sql(
            """
            CREATE VIRTUAL TABLE IF NOT EXISTS fts_pages
            USING fts5(
                text,
                content='pages',
                content_rowid='id',
                tokenize = 'unicode61'
            );
            """
        )

        # Триггеры синхронизации FTS с таблицей pages
        conn.exec_driver_sql(
            """
            CREATE TRIGGER IF NOT EXISTS pages_ai AFTER INSERT ON pages BEGIN
              INSERT INTO fts_pages(rowid, text) VALUES (new.id, new.text);
            END;
            """
        )
        conn.exec_driver_sql(
            """
            CREATE TRIGGER IF NOT EXISTS pages_ad AFTER DELETE ON pages BEGIN
              INSERT INTO fts_pages(fts_pages, rowid, text) VALUES('delete', old.id, old.text);
            END;
            """
        )
        conn.exec_driver_sql(
            """
            CREATE TRIGGER IF NOT EXISTS pages_au AFTER UPDATE ON pages BEGIN
              INSERT INTO fts_pages(fts_pages, rowid, text) VALUES('delete', old.id, old.text);
              INSERT INTO fts_pages(rowid, text) VALUES (new.id, new.text);
            END;
            """
        )

        conn.commit()
