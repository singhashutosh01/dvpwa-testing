"""Intentional extra sink for STO Codex incremental testing. Not for production."""

import subprocess

from aiohttp.web import Request, Response


async def ping(request: Request):
    host = request.query.get("host", "127.0.0.1")
    # User-controlled value is interpolated into a shell command.
    output = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return Response(text=output.decode(errors="replace"))
