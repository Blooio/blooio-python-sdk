# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .link_preview_param import LinkPreviewParam

__all__ = ["MessageSendParams", "Attachment", "AttachmentUnionObjectVariant1", "Part"]


class MessageSendParams(TypedDict, total=False):
    attachments: SequenceNotStr[Attachment]
    """Array of attachment URLs or objects with url/name"""

    from_number: str
    """E.164 phone number to send from.

    For Twilio API keys, this is optional — if omitted, the first assigned Twilio
    number is auto-selected. For Blooio (iMessage) API keys, this selects a specific
    number from your pool. Must be a number assigned to your API key.
    """

    link_preview: Optional[LinkPreviewParam]
    """Rich-link-preview overrides for URL messages (iMessage URL balloon).

    All fields are optional. Only applies when the message text (or the concatenated
    part text) is exactly a single http(s) URL. If omitted but the text is a URL,
    Blooio auto-fetches the page's Open Graph metadata to generate a preview. If the
    image download fails, the send still succeeds — Blooio silently falls back to
    the auto-generated preview.
    """

    parts: Iterable[Part]
    """Ordered array of message parts. Two modes:

    1. **Multipart mode** — parts sent as a single unified iMessage bubble (mix of
       text and attachment parts). This is the default.
    2. **URL-balloon batch mode** — triggered when any part has a `link_preview`
       object. Each part becomes its own rich-link-preview iMessage; parts are sent
       sequentially in array order. In batch mode every part must be text-only with
       `text` being a single http(s) URL. Response contains `message_ids[]` +
       `count` instead of `message_id`.
    """

    share_contact: bool
    """If true, the contact card (Name & Photo) will be shared with this message.

    The contact card is piggybacked onto the outgoing message. Defaults to false.
    """

    text: Union[str, SequenceNotStr[str]]
    """Message text.

    Can be a single string or array of strings (each becomes a separate message)
    """

    use_typing_indicator: bool
    """Whether to show typing indicator before sending. Defaults to org preference."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class AttachmentUnionObjectVariant1(TypedDict, total=False):
    url: Required[str]

    name: str


Attachment: TypeAlias = Union[str, AttachmentUnionObjectVariant1]


class Part(TypedDict, total=False):
    link_preview: Optional[LinkPreviewParam]
    """Rich-link-preview overrides for URL messages (iMessage URL balloon).

    All fields are optional. Only applies when the message text (or the concatenated
    part text) is exactly a single http(s) URL. If omitted but the text is a URL,
    Blooio auto-fetches the page's Open Graph metadata to generate a preview. If the
    image download fails, the send still succeeds — Blooio silently falls back to
    the auto-generated preview.
    """

    mention: str
    """Participant phone number or email to @-mention.

    Only valid with 'text'. The entire text of the part is rendered as the mention.
    """

    name: str
    """Filename for the attachment. Only valid with 'url'."""

    text: str
    """Text content for this part. Mutually exclusive with 'url'."""

    url: str
    """URL to an attachment for this part. Mutually exclusive with 'text'."""
