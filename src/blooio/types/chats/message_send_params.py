# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .link_preview_param import LinkPreviewParam

__all__ = ["MessageSendParams", "Attachment", "AttachmentUnionObjectVariant1", "Part", "ReplyTo"]


class MessageSendParams(TypedDict, total=False):
    attachments: SequenceNotStr[Attachment]
    """Array of attachment URLs or objects with url/name.

    **Voice memos:** a single audio file (`.mp3`, `.m4a`, `.wav`, `.aac`, `.opus`,
    `.ogg`) is automatically sent as a voice memo (the native waveform/scrubber
    bubble), not a plain audio-file attachment — no extra field is needed. A voice
    memo is a standalone bubble, so it cannot be combined with `text` or any other
    attachment; send the voice memo and the text as two separate messages.
    """

    effect: Optional[
        Literal[
            "slam",
            "loud",
            "gentle",
            "invisible-ink",
            "echo",
            "spotlight",
            "balloons",
            "confetti",
            "love",
            "lasers",
            "fireworks",
            "celebration",
            "none",
        ]
    ]
    """Optional. Attach an iMessage send-with-effect to the outgoing message.

    **Bubble effects** (apply to a single text bubble):

    - `slam` — Slam
    - `loud` — Loud
    - `gentle` — Gentle
    - `invisible-ink` — Invisible Ink

    **Screen effects** (full-screen animation in the recipient's chat):

    - `echo` — Echo
    - `spotlight` — Spotlight
    - `balloons` — Balloons
    - `confetti` — Confetti
    - `love` — Love (heart)
    - `lasers` — Lasers
    - `fireworks` — Fireworks
    - `celebration` — Celebration (sparkles)

    Values are case-insensitive and accept either dashes or spaces
    (`"Invisible Ink"` and `"invisible-ink"` both work). Pass `"none"` or omit the
    field to send without an effect.

    **Limitations:**

    - iMessage-only — when the chat is delivered as SMS or RCS the message is sent
      without an animation.
    - Not supported alongside the `parts` array (multipart bubbles cannot carry an
      effect). Use the top-level `text` field instead.
    - When `text` is an array, every message in the array is sent with the same
      effect.
    """

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

    reply_to: Optional[ReplyTo]
    """Inline-reply target on `POST /chats/{chatId}/messages`.

    Pass either `message_id` (preferred — references a Blooio-minted message) or
    `guid` (raw iMessage GUID, useful for replying to messages received before the
    row was minted in Blooio). The new send is dispatched to Lava with the resolved
    `selectedMessageGuid` + `partIndex`, which iMessage renders as an inline reply
    on the recipient's device.
    """

    share_contact: bool
    """If true, the contact card (Name & Photo) will be shared with this message.

    The contact card is piggybacked onto the outgoing message. Defaults to false. ⚠️
    Only available on **Dedicated Commercial** and **Dedicated Enterprise** plans —
    other plans receive a `403`.
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


class ReplyTo(TypedDict, total=False):
    """Inline-reply target on `POST /chats/{chatId}/messages`.

    Pass either `message_id` (preferred — references a Blooio-minted message) or `guid` (raw iMessage GUID, useful for replying to messages received before the row was minted in Blooio). The new send is dispatched to Lava with the resolved `selectedMessageGuid` + `partIndex`, which iMessage renders as an inline reply on the recipient's device.
    """

    guid: str
    """Raw iMessage GUID of the parent.

    When supplied without a `message_id`, Blooio attempts to look up the parent via
    `provider_message_guid`; if the parent isn't in our table the send still
    proceeds (Lava will thread on the device when possible) and the response carries
    `parent_unresolved: true`.
    """

    message_id: str
    """Blooio `message_id` of the parent.

    Must belong to the same chat, same from-number, and be no older than 30 days.
    Returns 404 `reply_target_not_found` if unknown.
    """

    part_index: int
    """Which part of the parent to reply to.

    Defaults to 0 (covers the 99% case of replying to a single-part text message).
    """
