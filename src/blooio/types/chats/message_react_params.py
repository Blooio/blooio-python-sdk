# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageReactParams"]


class MessageReactParams(TypedDict, total=False):
    chat_id: Required[Annotated[str, PropertyInfo(alias="chatId")]]

    reaction: Required[str]
    """The reaction to add or remove.

    Must be prefixed with `+` to add or `-` to remove.

    **Classic tapbacks:** `+love`, `-love`, `+like`, `-like`, `+dislike`,
    `-dislike`, `+laugh`, `-laugh`, `+emphasize`, `-emphasize`, `+question`,
    `-question`

    **Emoji reactions:** Any emoji prefixed with `+` or `-` (e.g. `+😂`, `-😂`,
    `+👍`, `-🔥`). Emoji reactions require macOS 14 (Sonoma) or later on the device.
    """

    direction: Literal["inbound", "outbound"]
    """
    Filter by message direction (only used when messageId is a relative index like
    -1, -2)
    """
