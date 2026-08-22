# Me

Types:

```python
from blooio.types import MeRetrieveResponse
```

Methods:

- <code title="get /me">client.me.<a href="./src/blooio/resources/me/me.py">retrieve</a>() -> <a href="./src/blooio/types/me_retrieve_response.py">MeRetrieveResponse</a></code>

## Numbers

Types:

```python
from blooio.types.me import NumberListResponse
```

Methods:

- <code title="get /me/numbers">client.me.numbers.<a href="./src/blooio/resources/me/numbers/numbers.py">list</a>() -> <a href="./src/blooio/types/me/number_list_response.py">NumberListResponse</a></code>

### ContactCard

Types:

```python
from blooio.types.me.numbers import ContactCardRetrieveResponse, ContactCardUpdateResponse
```

Methods:

- <code title="get /me/numbers/{number}/contact-card">client.me.numbers.contact_card.<a href="./src/blooio/resources/me/numbers/contact_card.py">retrieve</a>(number) -> <a href="./src/blooio/types/me/numbers/contact_card_retrieve_response.py">ContactCardRetrieveResponse</a></code>
- <code title="put /me/numbers/{number}/contact-card">client.me.numbers.contact_card.<a href="./src/blooio/resources/me/numbers/contact_card.py">update</a>(number, \*\*<a href="src/blooio/types/me/numbers/contact_card_update_params.py">params</a>) -> <a href="./src/blooio/types/me/numbers/contact_card_update_response.py">ContactCardUpdateResponse</a></code>

# Contacts

Types:

```python
from blooio.types import (
    Contact,
    DeleteResponse,
    Pagination,
    ContactListResponse,
    ContactCheckCapabilitiesResponse,
)
```

Methods:

- <code title="post /contacts">client.contacts.<a href="./src/blooio/resources/contacts/contacts.py">create</a>(\*\*<a href="src/blooio/types/contact_create_params.py">params</a>) -> <a href="./src/blooio/types/contact.py">Contact</a></code>
- <code title="get /contacts/{contactId}">client.contacts.<a href="./src/blooio/resources/contacts/contacts.py">retrieve</a>(contact_id) -> <a href="./src/blooio/types/contact.py">Contact</a></code>
- <code title="patch /contacts/{contactId}">client.contacts.<a href="./src/blooio/resources/contacts/contacts.py">update</a>(contact_id, \*\*<a href="src/blooio/types/contact_update_params.py">params</a>) -> <a href="./src/blooio/types/contact.py">Contact</a></code>
- <code title="get /contacts">client.contacts.<a href="./src/blooio/resources/contacts/contacts.py">list</a>(\*\*<a href="src/blooio/types/contact_list_params.py">params</a>) -> <a href="./src/blooio/types/contact_list_response.py">ContactListResponse</a></code>
- <code title="delete /contacts/{contactId}">client.contacts.<a href="./src/blooio/resources/contacts/contacts.py">delete</a>(contact_id) -> <a href="./src/blooio/types/delete_response.py">DeleteResponse</a></code>
- <code title="get /contacts/{contactId}/capabilities">client.contacts.<a href="./src/blooio/resources/contacts/contacts.py">check_capabilities</a>(contact_id) -> <a href="./src/blooio/types/contact_check_capabilities_response.py">ContactCheckCapabilitiesResponse</a></code>

## Tags

Types:

```python
from blooio.types.contacts import TagListResponse, TagAddResponse
```

Methods:

- <code title="get /contacts/{contactId}/tags">client.contacts.tags.<a href="./src/blooio/resources/contacts/tags.py">list</a>(contact_id) -> <a href="./src/blooio/types/contacts/tag_list_response.py">TagListResponse</a></code>
- <code title="post /contacts/{contactId}/tags">client.contacts.tags.<a href="./src/blooio/resources/contacts/tags.py">add</a>(contact_id, \*\*<a href="src/blooio/types/contacts/tag_add_params.py">params</a>) -> <a href="./src/blooio/types/contacts/tag_add_response.py">TagAddResponse</a></code>
- <code title="delete /contacts/{contactId}/tags/{tag}">client.contacts.tags.<a href="./src/blooio/resources/contacts/tags.py">remove</a>(tag, \*, contact_id) -> <a href="./src/blooio/types/delete_response.py">DeleteResponse</a></code>

# Location

## Contacts

Types:

```python
from blooio.types.location import ContactLocation, ContactListResponse, ContactRefreshResponse
```

Methods:

- <code title="get /location/contacts/{handle}">client.location.contacts.<a href="./src/blooio/resources/location/contacts.py">retrieve</a>(handle) -> <a href="./src/blooio/types/location/contact_location.py">ContactLocation</a></code>
- <code title="get /location/contacts">client.location.contacts.<a href="./src/blooio/resources/location/contacts.py">list</a>() -> <a href="./src/blooio/types/location/contact_list_response.py">ContactListResponse</a></code>
- <code title="post /location/contacts/refresh">client.location.contacts.<a href="./src/blooio/resources/location/contacts.py">refresh</a>() -> <a href="./src/blooio/types/location/contact_refresh_response.py">ContactRefreshResponse</a></code>

# Facetime

Types:

```python
from blooio.types import FacetimeInitiateCallResponse
```

Methods:

- <code title="post /facetime/calls">client.facetime.<a href="./src/blooio/resources/facetime.py">initiate_call</a>(\*\*<a href="src/blooio/types/facetime_initiate_call_params.py">params</a>) -> <a href="./src/blooio/types/facetime_initiate_call_response.py">FacetimeInitiateCallResponse</a></code>

# Groups

Types:

```python
from blooio.types import (
    Group,
    GroupCreateResponse,
    GroupUpdateResponse,
    GroupListResponse,
    GroupDeleteResponse,
)
```

Methods:

- <code title="post /groups">client.groups.<a href="./src/blooio/resources/groups/groups.py">create</a>(\*\*<a href="src/blooio/types/group_create_params.py">params</a>) -> <a href="./src/blooio/types/group_create_response.py">GroupCreateResponse</a></code>
- <code title="get /groups/{groupId}">client.groups.<a href="./src/blooio/resources/groups/groups.py">retrieve</a>(group_id) -> <a href="./src/blooio/types/group.py">Group</a></code>
- <code title="patch /groups/{groupId}">client.groups.<a href="./src/blooio/resources/groups/groups.py">update</a>(group_id, \*\*<a href="src/blooio/types/group_update_params.py">params</a>) -> <a href="./src/blooio/types/group_update_response.py">GroupUpdateResponse</a></code>
- <code title="get /groups">client.groups.<a href="./src/blooio/resources/groups/groups.py">list</a>(\*\*<a href="src/blooio/types/group_list_params.py">params</a>) -> <a href="./src/blooio/types/group_list_response.py">GroupListResponse</a></code>
- <code title="delete /groups/{groupId}">client.groups.<a href="./src/blooio/resources/groups/groups.py">delete</a>(group_id) -> <a href="./src/blooio/types/group_delete_response.py">GroupDeleteResponse</a></code>

## Members

Types:

```python
from blooio.types.groups import (
    GroupMember,
    MemberListResponse,
    MemberAddResponse,
    MemberRemoveResponse,
)
```

Methods:

- <code title="get /groups/{groupId}/members">client.groups.members.<a href="./src/blooio/resources/groups/members.py">list</a>(group_id, \*\*<a href="src/blooio/types/groups/member_list_params.py">params</a>) -> <a href="./src/blooio/types/groups/member_list_response.py">MemberListResponse</a></code>
- <code title="post /groups/{groupId}/members">client.groups.members.<a href="./src/blooio/resources/groups/members.py">add</a>(group_id, \*\*<a href="src/blooio/types/groups/member_add_params.py">params</a>) -> <a href="./src/blooio/types/groups/member_add_response.py">MemberAddResponse</a></code>
- <code title="delete /groups/{groupId}/members/{contactId}">client.groups.members.<a href="./src/blooio/resources/groups/members.py">remove</a>(contact_id, \*, group_id) -> <a href="./src/blooio/types/groups/member_remove_response.py">MemberRemoveResponse</a></code>

## Icon

Types:

```python
from blooio.types.groups import GroupIcon
```

Methods:

- <code title="delete /groups/{groupId}/icon">client.groups.icon.<a href="./src/blooio/resources/groups/icon.py">remove</a>(group_id) -> <a href="./src/blooio/types/groups/group_icon.py">GroupIcon</a></code>
- <code title="post /groups/{groupId}/icon">client.groups.icon.<a href="./src/blooio/resources/groups/icon.py">set</a>(group_id, \*\*<a href="src/blooio/types/groups/icon_set_params.py">params</a>) -> <a href="./src/blooio/types/groups/group_icon.py">GroupIcon</a></code>

# Webhooks

Types:

```python
from blooio.types import Webhook, WebhookCreateResponse, WebhookListResponse, WebhookDeleteResponse
```

Methods:

- <code title="post /webhooks">client.webhooks.<a href="./src/blooio/resources/webhooks/webhooks.py">create</a>(\*\*<a href="src/blooio/types/webhook_create_params.py">params</a>) -> <a href="./src/blooio/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /webhooks/{webhookId}">client.webhooks.<a href="./src/blooio/resources/webhooks/webhooks.py">retrieve</a>(webhook_id) -> <a href="./src/blooio/types/webhook.py">Webhook</a></code>
- <code title="patch /webhooks/{webhookId}">client.webhooks.<a href="./src/blooio/resources/webhooks/webhooks.py">update</a>(webhook_id, \*\*<a href="src/blooio/types/webhook_update_params.py">params</a>) -> <a href="./src/blooio/types/webhook.py">Webhook</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/blooio/resources/webhooks/webhooks.py">list</a>() -> <a href="./src/blooio/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /webhooks/{webhookId}">client.webhooks.<a href="./src/blooio/resources/webhooks/webhooks.py">delete</a>(webhook_id) -> <a href="./src/blooio/types/webhook_delete_response.py">WebhookDeleteResponse</a></code>

## Secret

Types:

```python
from blooio.types.webhooks import SecretRotateResponse
```

Methods:

- <code title="post /webhooks/{webhookId}/secret/rotate">client.webhooks.secret.<a href="./src/blooio/resources/webhooks/secret.py">rotate</a>(webhook_id) -> <a href="./src/blooio/types/webhooks/secret_rotate_response.py">SecretRotateResponse</a></code>

## Logs

Types:

```python
from blooio.types.webhooks import LogListResponse, LogReplayResponse
```

Methods:

- <code title="get /webhooks/{webhookId}/logs">client.webhooks.logs.<a href="./src/blooio/resources/webhooks/logs.py">list</a>(webhook_id, \*\*<a href="src/blooio/types/webhooks/log_list_params.py">params</a>) -> <a href="./src/blooio/types/webhooks/log_list_response.py">LogListResponse</a></code>
- <code title="post /webhooks/{webhookId}/logs/{eventId}/replay">client.webhooks.logs.<a href="./src/blooio/resources/webhooks/logs.py">replay</a>(event_id, \*, webhook_id) -> <a href="./src/blooio/types/webhooks/log_replay_response.py">LogReplayResponse</a></code>

# Chats

Types:

```python
from blooio.types import (
    LastMessage,
    ChatRetrieveResponse,
    ChatListResponse,
    ChatMarkAsReadResponse,
    ChatShareContactCardResponse,
)
```

Methods:

- <code title="get /chats/{chatId}">client.chats.<a href="./src/blooio/resources/chats/chats.py">retrieve</a>(chat_id) -> <a href="./src/blooio/types/chat_retrieve_response.py">ChatRetrieveResponse</a></code>
- <code title="get /chats">client.chats.<a href="./src/blooio/resources/chats/chats.py">list</a>(\*\*<a href="src/blooio/types/chat_list_params.py">params</a>) -> <a href="./src/blooio/types/chat_list_response.py">ChatListResponse</a></code>
- <code title="post /chats/{chatId}/read">client.chats.<a href="./src/blooio/resources/chats/chats.py">mark_as_read</a>(chat_id) -> <a href="./src/blooio/types/chat_mark_as_read_response.py">ChatMarkAsReadResponse</a></code>
- <code title="post /chats/{chatId}/contact-card">client.chats.<a href="./src/blooio/resources/chats/chats.py">share_contact_card</a>(chat_id) -> <a href="./src/blooio/types/chat_share_contact_card_response.py">ChatShareContactCardResponse</a></code>

## Messages

Types:

```python
from blooio.types.chats import (
    LinkPreview,
    Reaction,
    MessageRetrieveResponse,
    MessageListResponse,
    MessageGetStatusResponse,
    MessageReactResponse,
    MessageSendResponse,
)
```

Methods:

- <code title="get /chats/{chatId}/messages/{messageId}">client.chats.messages.<a href="./src/blooio/resources/chats/messages.py">retrieve</a>(message_id, \*, chat_id) -> <a href="./src/blooio/types/chats/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="get /chats/{chatId}/messages">client.chats.messages.<a href="./src/blooio/resources/chats/messages.py">list</a>(chat_id, \*\*<a href="src/blooio/types/chats/message_list_params.py">params</a>) -> <a href="./src/blooio/types/chats/message_list_response.py">MessageListResponse</a></code>
- <code title="get /chats/{chatId}/messages/{messageId}/status">client.chats.messages.<a href="./src/blooio/resources/chats/messages.py">get_status</a>(message_id, \*, chat_id) -> <a href="./src/blooio/types/chats/message_get_status_response.py">MessageGetStatusResponse</a></code>
- <code title="post /chats/{chatId}/messages/{messageId}/reactions">client.chats.messages.<a href="./src/blooio/resources/chats/messages.py">react</a>(message_id, \*, chat_id, \*\*<a href="src/blooio/types/chats/message_react_params.py">params</a>) -> <a href="./src/blooio/types/chats/message_react_response.py">MessageReactResponse</a></code>
- <code title="post /chats/{chatId}/messages">client.chats.messages.<a href="./src/blooio/resources/chats/messages.py">send</a>(chat_id, \*\*<a href="src/blooio/types/chats/message_send_params.py">params</a>) -> <a href="./src/blooio/types/chats/message_send_response.py">MessageSendResponse</a></code>

## Polls

Types:

```python
from blooio.types.chats import PollGetResultsResponse, PollSendResponse
```

Methods:

- <code title="get /chats/{chatId}/polls/{pollId}">client.chats.polls.<a href="./src/blooio/resources/chats/polls.py">get_results</a>(poll_id, \*, chat_id) -> <a href="./src/blooio/types/chats/poll_get_results_response.py">PollGetResultsResponse</a></code>
- <code title="post /chats/{chatId}/polls">client.chats.polls.<a href="./src/blooio/resources/chats/polls.py">send</a>(chat_id, \*\*<a href="src/blooio/types/chats/poll_send_params.py">params</a>) -> <a href="./src/blooio/types/chats/poll_send_response.py">PollSendResponse</a></code>

## Typing

Types:

```python
from blooio.types.chats import TypingResponse
```

Methods:

- <code title="post /chats/{chatId}/typing">client.chats.typing.<a href="./src/blooio/resources/chats/typing.py">start</a>(chat_id) -> <a href="./src/blooio/types/chats/typing_response.py">TypingResponse</a></code>
- <code title="delete /chats/{chatId}/typing">client.chats.typing.<a href="./src/blooio/resources/chats/typing.py">stop</a>(chat_id) -> <a href="./src/blooio/types/chats/typing_response.py">TypingResponse</a></code>

## Background

Types:

```python
from blooio.types.chats import ChatBackgroundResponse
```

Methods:

- <code title="get /chats/{chatId}/background">client.chats.background.<a href="./src/blooio/resources/chats/background.py">retrieve</a>(chat_id) -> <a href="./src/blooio/types/chats/chat_background_response.py">ChatBackgroundResponse</a></code>
- <code title="delete /chats/{chatId}/background">client.chats.background.<a href="./src/blooio/resources/chats/background.py">remove</a>(chat_id) -> <a href="./src/blooio/types/chats/chat_background_response.py">ChatBackgroundResponse</a></code>
- <code title="put /chats/{chatId}/background">client.chats.background.<a href="./src/blooio/resources/chats/background.py">set</a>(chat_id, \*\*<a href="src/blooio/types/chats/background_set_params.py">params</a>) -> <a href="./src/blooio/types/chats/chat_background_response.py">ChatBackgroundResponse</a></code>

# PhoneNumbers

Types:

```python
from blooio.types import PhoneNumberBatchCreateResponse
```

Methods:

- <code title="post /phone-numbers/batch">client.phone_numbers.<a href="./src/blooio/resources/phone_numbers/phone_numbers.py">batch_create</a>(\*\*<a href="src/blooio/types/phone_number_batch_create_params.py">params</a>) -> <a href="./src/blooio/types/phone_number_batch_create_response.py">PhoneNumberBatchCreateResponse</a></code>

## Lookup

Types:

```python
from blooio.types.phone_numbers import PhoneNumberLookupResult
```

Methods:

- <code title="post /phone-numbers/lookup">client.phone_numbers.lookup.<a href="./src/blooio/resources/phone_numbers/lookup.py">create</a>(\*\*<a href="src/blooio/types/phone_numbers/lookup_create_params.py">params</a>) -> <a href="./src/blooio/types/phone_numbers/phone_number_lookup_result.py">PhoneNumberLookupResult</a></code>
- <code title="get /phone-numbers/lookup">client.phone_numbers.lookup.<a href="./src/blooio/resources/phone_numbers/lookup.py">retrieve</a>(\*\*<a href="src/blooio/types/phone_numbers/lookup_retrieve_params.py">params</a>) -> <a href="./src/blooio/types/phone_numbers/phone_number_lookup_result.py">PhoneNumberLookupResult</a></code>
