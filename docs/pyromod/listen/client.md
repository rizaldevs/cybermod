### *class* cybermod.listen.Client

Bases: `cybergram.Client`

### *async* listen(filters: Filter | None = None, listener_type: [ListenerTypes](/build/markdown/cybermod.types#cybermod.types.listener_types.ListenerTypes) = ListenerTypes.MESSAGE, timeout: int | None = None, unallowed_click_alert: bool = True, chat_id: int | None = None, user_id: int | None = None, message_id: int | None = None, inline_message_id: str | None = None)

Listen for a message, callback query, etc.

* **Parameters:**
    * **filters** (*cybergram.filters.Filter* *or* *None*) – A filter to check the incoming message against.
    * **listener_type** (*cybermod.types.ListenerTypes*) – The type of listener to listen for.
    * **timeout** (*int* *or* *None*) – The maximum amount of time to wait for a message.
    * **unallowed_click_alert** (*bool*) – Whether to alert the user if they click a button that doesn’t match the
      filters.
    * **chat_id** (*int* *or* *None*) – The chat ID to listen for.
    * **user_id** (*int* *or* *None*) – The user ID to listen for.
    * **message_id** (*int* *or* *None*) – The message ID to listen for.
    * **inline_message_id** (*str* *or* *None*) – The inline message ID to listen for.
* **Raises:**
    * **cybermod.exceptions.ListenerStopped** – If the listener was stopped.
    * **cybermod.exceptions.ListenerTimeout** – If the listener timed out.
* **Returns:**
  The message that was listened for.
* **Return type:**
  cybergram.types.Message or cybergram.types.CallbackQuery

### *async* ask(chat_id: int, text: str, filters: Filter | None = None, listener_type: [ListenerTypes](/build/markdown/cybermod.types#cybermod.types.listener_types.ListenerTypes) = ListenerTypes.MESSAGE, timeout: int | None = None, unallowed_click_alert: bool = True, user_id: int | None = None, message_id: int | None = None, inline_message_id: str | None = None, \*args, \*\*kwargs)

Send a message and calls Client.listen to wait for a response.

* **Parameters:**
    * **chat_id** (*int*) – The chat ID to send the message to. It will also be used to listen for a response.
    * **text** (*str*) – The text of the message to send.
    * **filters** (*cybergram.filters.Filter* *or* *None*) – A filter to check the incoming message against.
    * **listener_type** (*cybermod.types.ListenerTypes*) – The type of listener to listen for.
    * **timeout** (*int* *or* *None*) – The maximum amount of time to wait for a message.
    * **unallowed_click_alert** (*bool*) – Whether to alert the user if they click a button that doesn’t match the
      filters.
    * **user_id** (*int* *or* *None*) – The user ID to listen for.
    * **message_id** (*int* *or* *None*) – The message ID to listen for.
    * **inline_message_id** (*str* *or* *None*) – The inline message ID to listen for.
    * **args** –
    * **kwargs** –
* **Returns:**
  The message that was listened for. In the attribute `request` you can find the message that was sent.
* **Return type:**
  cybergram.types.Message or cybergram.types.CallbackQuery

### get_matching_listener(pattern: [Identifier](/build/markdown/cybermod.types#cybermod.types.identifier.Identifier), listener_type: [ListenerTypes](/build/markdown/cybermod.types#cybermod.types.listener_types.ListenerTypes))

Get a listener that matches the given pattern.

* **Parameters:**
    * **pattern** (*cybermod.types.Identifier*) –
    * **listener_type** (*cybermod.types.ListenerTypes*) –
* **Returns:**
  The listener that matches the given pattern.
* **Return type:**
  cybermod.types.Listener or None

### get_many_matching_listeners(pattern: [Identifier](/build/markdown/cybermod.types#cybermod.types.identifier.Identifier), listener_type: [ListenerTypes](/build/markdown/cybermod.types#cybermod.types.listener_types.ListenerTypes))

Get all listeners that match the given pattern.

* **Parameters:**
    * **pattern** (*cybermod.types.Identifier*) –
    * **listener_type** (*cybermod.types.ListenerTypes*) –
* **Returns:**
  All listeners that match the given pattern.
* **Return type:**
  list[cybermod.types.Listener]

### remove_listener(listener: [Listener](/build/markdown/cybermod.types#cybermod.types.listener.Listener))

Remove a listener.

* **Parameters:**
  **listener** (*cybermod.types.Listener*) –
* **Returns:**
  None

### stop_listening(listener_type: [ListenerTypes](/build/markdown/cybermod.types#cybermod.types.listener_types.ListenerTypes) = ListenerTypes.MESSAGE, chat_id: int | None = None, user_id: int | None = None, message_id: int | None = None, inline_message_id: str | None = None)

Stop listening for a message, callback query, etc.

* **Parameters:**
    * **listener_type** (*cybermod.types.ListenerTypes*) – The type of listener to stop listening for.
    * **chat_id** (*int* *or* *None*) – The chat ID to stop listening for.
    * **user_id** (*int* *or* *None*) – The user ID to stop listening for.
    * **message_id** (*int* *or* *None*) – The message ID to stop listening for.
    * **inline_message_id** (*str* *or* *None*) – The inline message ID to stop listening for.
* **Returns:**
  None

### listeners*: dict[[ListenerTypes](/build/markdown/cybermod.types#cybermod.types.listener_types.ListenerTypes), list[[Listener](/build/markdown/cybermod.types#cybermod.types.listener.Listener)]]*