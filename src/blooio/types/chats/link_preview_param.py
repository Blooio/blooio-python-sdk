# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LinkPreviewParam"]


class LinkPreviewParam(TypedDict, total=False):
    """Rich-link-preview overrides for URL messages (iMessage URL balloon).

    All fields are optional. Only applies when the message text (or the concatenated part text) is exactly a single http(s) URL. If omitted but the text is a URL, Blooio auto-fetches the page's Open Graph metadata to generate a preview. If the image download fails, the send still succeeds — Blooio silently falls back to the auto-generated preview.
    """

    image_url: str
    """HTTPS URL to an image (png, jpg, webp, gif).

    Blooio downloads the image server-side and attaches it as the rich-link hero.
    Max 16 MB. If the download fails or returns a non-image MIME, the send falls
    back to auto-fetched OG metadata.
    """

    title: str
    """Bold title line rendered in the iMessage bubble.

    Overrides the page's `<meta property="og:title">`.
    """
