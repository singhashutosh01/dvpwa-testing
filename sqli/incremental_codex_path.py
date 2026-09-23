"""Intentional extra sink for STO Codex incremental testing. Not for production."""

from aiohttp.web import Request, Response


async def read_file(request: Request):
    name = request.query.get("file", "README.md")
    # User-controlled path is opened directly (path traversal).
    with open(name, encoding="utf-8", errors="replace") as handle:
        body = handle.read()
    return Response(text=body)
