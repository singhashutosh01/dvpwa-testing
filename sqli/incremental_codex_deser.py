"""Intentional extra sink for STO Codex incremental testing. Not for production."""

import pickle
from base64 import b64decode

from aiohttp.web import Request, Response


async def load_object(request: Request):
    payload = request.query.get("payload", "")
    # User-controlled bytes are deserialized with pickle (insecure deserialization).
    obj = pickle.loads(b64decode(payload))
    return Response(text=repr(obj))
