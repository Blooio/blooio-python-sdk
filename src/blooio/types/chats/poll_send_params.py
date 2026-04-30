# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["PollSendParams"]


class PollSendParams(TypedDict, total=False):
    options: Required[SequenceNotStr[str]]
    """Array of 2-10 option strings for the poll"""

    title: str
    """Poll question or title (optional)"""
