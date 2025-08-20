from __future__ import annotations

from typing import Any, Dict, List
from sqlalchemy import text

from docsearch.db.session import engine


def search_pages(query: str, limit: int = 20) -> List[Dict[str, Any]]:
    """Выполняет полнотекстовый поиск по страницам через SQLite FTS5.

    Возвращает список результатов: page_id, document_id, page_no, snippet.
    Если запрос пустой/короткий, возвращает пустой список.
    """
    q = (query or "").strip()
    if not q:
        return []

    sql = text(
        """
        SELECT p.id AS page_id,
               p.document_id AS document_id,
               p.page_no AS page_no,
               snippet(fts_pages, 0, '<mark>', '</mark>', '…', 10) AS snippet,
               bm25(fts_pages) AS score
        FROM fts_pages
        JOIN pages AS p ON p.id = fts_pages.rowid
        WHERE fts_pages MATCH :q
        ORDER BY score ASC
        LIMIT :k
        """
    )

    with engine.connect() as conn:
        rows = conn.execute(sql, {"q": q, "k": limit}).mappings().all()
        return [dict(row) for row in rows]
