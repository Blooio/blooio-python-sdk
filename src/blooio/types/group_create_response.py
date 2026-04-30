# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .group import Group

__all__ = ["GroupCreateResponse"]


class GroupCreateResponse(Group):
    added_members: Optional[List[str]] = None
    """List of member identifiers that were added to the group"""

    created_contacts: Optional[List[str]] = None
    """List of contacts that were auto-created"""
