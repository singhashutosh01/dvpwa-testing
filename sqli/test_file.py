"""Intentional extra sink for STO Claude incremental testing. Not for production."""

import hashlib

from aiohttp.web import Request, Response

# Fixture value so the incremental diff has a new finding. Not a real secret.
_FIXTURE_PASSWORD = "claude-incremental-fixture"


async def check_token(request: Request):
    supplied = request.query.get("token", "")
    digest = hashlib.md5(supplied.encode()).hexdigest()
    expected = hashlib.md5(_FIXTURE_PASSWORD.encode()).hexdigest()
    if digest == expected:
        return Response(text="ok")
    return Response(status=401, text="no")
