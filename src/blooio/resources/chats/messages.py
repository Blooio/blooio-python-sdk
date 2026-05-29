# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.chats import message_list_params, message_send_params, message_react_params
from ..._base_client import make_request_options
from ...types.chats.link_preview_param import LinkPreviewParam
from ...types.chats.message_list_response import MessageListResponse
from ...types.chats.message_send_response import MessageSendResponse
from ...types.chats.message_react_response import MessageReactResponse
from ...types.chats.message_retrieve_response import MessageRetrieveResponse
from ...types.chats.message_get_status_response import MessageGetStatusResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        message_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Get details for a specific message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            path_template("/chats/{chat_id}/messages/{message_id}", chat_id=chat_id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    def list(
        self,
        chat_id: str,
        *,
        direction: Literal["inbound", "outbound"] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        since: int | Omit = omit,
        sort: Literal["asc", "desc"] | Omit = omit,
        until: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        List all messages in a conversation with optional filtering.

        Args:
          direction: Filter by message direction

          limit: Maximum number of items to return (1-200)

          offset: Number of items to skip

          since: Only messages sent after this timestamp (ms)

          sort: Sort order by time

          until: Only messages sent before this timestamp (ms)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            path_template("/chats/{chat_id}/messages", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "offset": offset,
                        "since": since,
                        "sort": sort,
                        "until": until,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    def get_status(
        self,
        message_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageGetStatusResponse:
        """
        Get delivery status for a specific message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            path_template("/chats/{chat_id}/messages/{message_id}/status", chat_id=chat_id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageGetStatusResponse,
        )

    def react(
        self,
        message_id: str,
        *,
        chat_id: str,
        reaction: str,
        direction: Literal["inbound", "outbound"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageReactResponse:
        """Add or remove a reaction to a message.

        Supports classic iMessage tapbacks (love,
        like, dislike, laugh, emphasize, question) and emoji reactions (e.g. +😂, -😂).

        The messageId can be an explicit message ID (e.g., msg_xxx) or a relative index
        (-1 for last message, -2 for second-to-last, etc.). When using relative indices,
        you can optionally filter by message direction (inbound/outbound only).

        Args:
          reaction: The reaction to add or remove. Must be prefixed with `+` to add or `-` to
              remove.

              **Classic tapbacks:** `+love`, `-love`, `+like`, `-like`, `+dislike`,
              `-dislike`, `+laugh`, `-laugh`, `+emphasize`, `-emphasize`, `+question`,
              `-question`

              **Emoji reactions:** Any emoji prefixed with `+` or `-` (e.g. `+😂`, `-😂`,
              `+👍`, `-🔥`).

          direction: Filter by message direction (only used when messageId is a relative index like
              -1, -2)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template("/chats/{chat_id}/messages/{message_id}/reactions", chat_id=chat_id, message_id=message_id),
            body=maybe_transform(
                {
                    "reaction": reaction,
                    "direction": direction,
                },
                message_react_params.MessageReactParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageReactResponse,
        )

    def send(
        self,
        chat_id: str,
        *,
        attachments: SequenceNotStr[message_send_params.Attachment] | Omit = omit,
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
        | Omit = omit,
        from_number: str | Omit = omit,
        link_preview: Optional[LinkPreviewParam] | Omit = omit,
        parts: Iterable[message_send_params.Part] | Omit = omit,
        share_contact: bool | Omit = omit,
        text: Union[str, SequenceNotStr[str]] | Omit = omit,
        use_typing_indicator: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """Send a message to a chat.

        The chatId can be: (1) E.164 phone number, (2) email
        address, (3) group ID (grp_xxxx), or (4) comma-separated list of phone/email for
        multi-recipient chats. For multi-recipient, an unnamed group is automatically
        created or reused if the exact participant combination already exists. For
        explicit groups, the group must be linked to an existing iMessage chat.

        **iMessage send-with-effect:** set the optional `effect` field to attach an
        Apple expressive send (slam, loud, gentle, invisible-ink) or screen effect
        (echo, spotlight, balloons, confetti, love, lasers, fireworks, celebration).
        Effects are an iMessage-only feature — when the recipient is on SMS/RCS the
        message is delivered without the animation. Effects are not supported in
        multipart (`parts`) mode.

        Args:
          attachments: Array of attachment URLs or objects with url/name

          effect: Optional. Attach an iMessage send-with-effect to the outgoing message.

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

          from_number: E.164 phone number to send from. For Twilio API keys, this is optional — if
              omitted, the first assigned Twilio number is auto-selected. For Blooio
              (iMessage) API keys, this selects a specific number from your pool. Must be a
              number assigned to your API key.

          link_preview: Rich-link-preview overrides for URL messages (iMessage URL balloon). All fields
              are optional. Only applies when the message text (or the concatenated part text)
              is exactly a single http(s) URL. If omitted but the text is a URL, Blooio
              auto-fetches the page's Open Graph metadata to generate a preview. If the image
              download fails, the send still succeeds — Blooio silently falls back to the
              auto-generated preview.

          parts:
              Ordered array of message parts. Two modes:

              1. **Multipart mode** — parts sent as a single unified iMessage bubble (mix of
                 text and attachment parts). This is the default.
              2. **URL-balloon batch mode** — triggered when any part has a `link_preview`
                 object. Each part becomes its own rich-link-preview iMessage; parts are sent
                 sequentially in array order. In batch mode every part must be text-only with
                 `text` being a single http(s) URL. Response contains `message_ids[]` +
                 `count` instead of `message_id`.

          share_contact: If true, the contact card (Name & Photo) will be shared with this message. The
              contact card is piggybacked onto the outgoing message. Defaults to false. ⚠️
              Only available on **Dedicated Commercial** and **Dedicated Enterprise** plans —
              other plans receive a `403`.

          text: Message text. Can be a single string or array of strings (each becomes a
              separate message)

          use_typing_indicator: Whether to show typing indicator before sending. Defaults to org preference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/chats/{chat_id}/messages", chat_id=chat_id),
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "effect": effect,
                    "from_number": from_number,
                    "link_preview": link_preview,
                    "parts": parts,
                    "share_contact": share_contact,
                    "text": text,
                    "use_typing_indicator": use_typing_indicator,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        message_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Get details for a specific message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            path_template("/chats/{chat_id}/messages/{message_id}", chat_id=chat_id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    async def list(
        self,
        chat_id: str,
        *,
        direction: Literal["inbound", "outbound"] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        since: int | Omit = omit,
        sort: Literal["asc", "desc"] | Omit = omit,
        until: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        List all messages in a conversation with optional filtering.

        Args:
          direction: Filter by message direction

          limit: Maximum number of items to return (1-200)

          offset: Number of items to skip

          since: Only messages sent after this timestamp (ms)

          sort: Sort order by time

          until: Only messages sent before this timestamp (ms)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            path_template("/chats/{chat_id}/messages", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "offset": offset,
                        "since": since,
                        "sort": sort,
                        "until": until,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    async def get_status(
        self,
        message_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageGetStatusResponse:
        """
        Get delivery status for a specific message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            path_template("/chats/{chat_id}/messages/{message_id}/status", chat_id=chat_id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageGetStatusResponse,
        )

    async def react(
        self,
        message_id: str,
        *,
        chat_id: str,
        reaction: str,
        direction: Literal["inbound", "outbound"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageReactResponse:
        """Add or remove a reaction to a message.

        Supports classic iMessage tapbacks (love,
        like, dislike, laugh, emphasize, question) and emoji reactions (e.g. +😂, -😂).

        The messageId can be an explicit message ID (e.g., msg_xxx) or a relative index
        (-1 for last message, -2 for second-to-last, etc.). When using relative indices,
        you can optionally filter by message direction (inbound/outbound only).

        Args:
          reaction: The reaction to add or remove. Must be prefixed with `+` to add or `-` to
              remove.

              **Classic tapbacks:** `+love`, `-love`, `+like`, `-like`, `+dislike`,
              `-dislike`, `+laugh`, `-laugh`, `+emphasize`, `-emphasize`, `+question`,
              `-question`

              **Emoji reactions:** Any emoji prefixed with `+` or `-` (e.g. `+😂`, `-😂`,
              `+👍`, `-🔥`).

          direction: Filter by message direction (only used when messageId is a relative index like
              -1, -2)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template("/chats/{chat_id}/messages/{message_id}/reactions", chat_id=chat_id, message_id=message_id),
            body=await async_maybe_transform(
                {
                    "reaction": reaction,
                    "direction": direction,
                },
                message_react_params.MessageReactParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageReactResponse,
        )

    async def send(
        self,
        chat_id: str,
        *,
        attachments: SequenceNotStr[message_send_params.Attachment] | Omit = omit,
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
        | Omit = omit,
        from_number: str | Omit = omit,
        link_preview: Optional[LinkPreviewParam] | Omit = omit,
        parts: Iterable[message_send_params.Part] | Omit = omit,
        share_contact: bool | Omit = omit,
        text: Union[str, SequenceNotStr[str]] | Omit = omit,
        use_typing_indicator: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """Send a message to a chat.

        The chatId can be: (1) E.164 phone number, (2) email
        address, (3) group ID (grp_xxxx), or (4) comma-separated list of phone/email for
        multi-recipient chats. For multi-recipient, an unnamed group is automatically
        created or reused if the exact participant combination already exists. For
        explicit groups, the group must be linked to an existing iMessage chat.

        **iMessage send-with-effect:** set the optional `effect` field to attach an
        Apple expressive send (slam, loud, gentle, invisible-ink) or screen effect
        (echo, spotlight, balloons, confetti, love, lasers, fireworks, celebration).
        Effects are an iMessage-only feature — when the recipient is on SMS/RCS the
        message is delivered without the animation. Effects are not supported in
        multipart (`parts`) mode.

        Args:
          attachments: Array of attachment URLs or objects with url/name

          effect: Optional. Attach an iMessage send-with-effect to the outgoing message.

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

          from_number: E.164 phone number to send from. For Twilio API keys, this is optional — if
              omitted, the first assigned Twilio number is auto-selected. For Blooio
              (iMessage) API keys, this selects a specific number from your pool. Must be a
              number assigned to your API key.

          link_preview: Rich-link-preview overrides for URL messages (iMessage URL balloon). All fields
              are optional. Only applies when the message text (or the concatenated part text)
              is exactly a single http(s) URL. If omitted but the text is a URL, Blooio
              auto-fetches the page's Open Graph metadata to generate a preview. If the image
              download fails, the send still succeeds — Blooio silently falls back to the
              auto-generated preview.

          parts:
              Ordered array of message parts. Two modes:

              1. **Multipart mode** — parts sent as a single unified iMessage bubble (mix of
                 text and attachment parts). This is the default.
              2. **URL-balloon batch mode** — triggered when any part has a `link_preview`
                 object. Each part becomes its own rich-link-preview iMessage; parts are sent
                 sequentially in array order. In batch mode every part must be text-only with
                 `text` being a single http(s) URL. Response contains `message_ids[]` +
                 `count` instead of `message_id`.

          share_contact: If true, the contact card (Name & Photo) will be shared with this message. The
              contact card is piggybacked onto the outgoing message. Defaults to false. ⚠️
              Only available on **Dedicated Commercial** and **Dedicated Enterprise** plans —
              other plans receive a `403`.

          text: Message text. Can be a single string or array of strings (each becomes a
              separate message)

          use_typing_indicator: Whether to show typing indicator before sending. Defaults to org preference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/chats/{chat_id}/messages", chat_id=chat_id),
            body=await async_maybe_transform(
                {
                    "attachments": attachments,
                    "effect": effect,
                    "from_number": from_number,
                    "link_preview": link_preview,
                    "parts": parts,
                    "share_contact": share_contact,
                    "text": text,
                    "use_typing_indicator": use_typing_indicator,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.get_status = to_raw_response_wrapper(
            messages.get_status,
        )
        self.react = to_raw_response_wrapper(
            messages.react,
        )
        self.send = to_raw_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.get_status = async_to_raw_response_wrapper(
            messages.get_status,
        )
        self.react = async_to_raw_response_wrapper(
            messages.react,
        )
        self.send = async_to_raw_response_wrapper(
            messages.send,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.get_status = to_streamed_response_wrapper(
            messages.get_status,
        )
        self.react = to_streamed_response_wrapper(
            messages.react,
        )
        self.send = to_streamed_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.get_status = async_to_streamed_response_wrapper(
            messages.get_status,
        )
        self.react = async_to_streamed_response_wrapper(
            messages.react,
        )
        self.send = async_to_streamed_response_wrapper(
            messages.send,
        )
