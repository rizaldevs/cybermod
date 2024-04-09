###  *function* cybermod.array_chunk(input_array, size)

Split an array into chunks.

* **Parameters:**
    * **input_array** – The array to split.
    * **size** – The size of each chunk.
* **Returns:**
  A list of chunks.

###  *function* cybermod.bki(keyboard)

Deserialize an InlineKeyboardMarkup to a list of lists of buttons.

* **Parameters:**
  **keyboard** – An InlineKeyboardMarkup.
* **Returns:**
  A list of lists of buttons.

###  *function* cybermod.btn(text, value, type='callback_data')

Create an InlineKeyboardButton.

* **Parameters:**
    * **text** – The text of the button.
    * **value** – The value of the button.
    * **type** – The type of the button.
* **Returns:**
  An InlineKeyboardButton.

###  *function* cybermod.force_reply(selective=True)

Create a ForceReply.

* **Parameters:**
  **selective** – Whether the reply should be selective.
* **Returns:**
  A ForceReply.

###  *function* cybermod.ikb(rows=None)

Create an InlineKeyboardMarkup from a list of lists of buttons.

* **Parameters:**
  **rows** – A list of lists of buttons.
* **Returns:**
  An InlineKeyboardMarkup.

###  *function* cybermod.kb(rows=None, \*\*kwargs)

Create a ReplyKeyboardMarkup from a list of lists of buttons.

* **Parameters:**
    * **rows** – A list of lists of buttons.
    * **kwargs** – Keyword arguments to pass to ReplyKeyboardMarkup.
* **Returns:**
  A ReplyKeyboardMarkup.

###  *function* cybermod.kbtn

alias of `KeyboardButton`

###  *function* cybermod.ntb(button)

Deserialize an InlineKeyboardButton to btn() format.

* **Parameters:**
  **button** – An InlineKeyboardButton.
* **Returns:**
  A btn() format button.
