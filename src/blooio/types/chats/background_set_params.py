# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["BackgroundSetParams"]


class BackgroundSetParams(TypedDict, total=False):
    background: Required[FileTypes]
    """Binary image file upload (JPEG, PNG, GIF, WebP, HEIC/HEIF, max 10 MB).

    Send as a file field in `multipart/form-data` — e.g.
    `-F "background=@/path/to/image.jpg"` with curl, or a `File`/`Blob` appended to
    `FormData` in JavaScript. Do NOT send a URL or base64 string.
    """
