# Changelog from cybermod v2 to v3
"""
- The classes Client, Message, Chat and User now inherit from their respective classes in cybergram. This mean you can use them as if they were the original classes from cybergram. This is super useful for the IDEs to provide code completion and type checking of the cybermod features.
- Since we can now use cybermod's Client just like the original Client, there is a new way of initilizing cybermod. Before, you needed to import cybermod anywhere in your code before importing cybergram. Now you can simply import Client from cybermod instead of cybergram and you are good to go.
- The decorators patch and patchable have been renamed to patch_into and should_patch respectively, making them more descriptive.
- The tuple identifiers that divided opinions have been removed. Now you can specify the data directly to the listen and ask methods as keyword arguments.
- Added support for inline_message_id in the listen and ask methods.
- cybermod will now check if the CallbackQuery.chat exists before trying to get its id, since it will be null on inline messages.
- The order of the arguments of Client.ask has been changed. Now the first argument is the chat_id and the second is the text to send, following the same order as Client.send_message.
- The internal login of listeners got a lot more simple and robust. It has been hugely refactored and now it's a lot easier to understand and maintain.
- The internal logic of the listeners state has been refactored. Now it uses Listener objects instead of a bunch of positional variables and dicts.
- The whole code got type hints. This means that the IDEs can now provide code completion and type checking of the cybermod features.
- The classes Client, Chat, User, Message, MessageHandler and CallbackQueryHAndler, that were previously in the listen.py file were split into their own files into the listen subpackage.
- The classes ListenerStopped and ListenerTimeout, that were previously in the listen.py file were moved to the exceptions subpackage.
- The class cybergramConfig, that was previously in the utils.py file was moved to the config subpackage. It's now called config and it's a SimpleNamespace object instead of a class.
- The enum ListenerTypes, that was previously in the listen.py file was moved to the types subpackage.
- Now the ask method will only send a message if the specified text is not empty. Thanks for that, @Eikosa!
- The attribute request of the Message object returned by the ask method has been renamed to sent_message, much more descriptive. Thanks again, @Eikosa!
- @tofikdn has added support for Message.message_id, when available, like in cybergram v1. Thanks for that!
- @Jusidama-Bot made a huge contribution to the project, making the monkeypatching utils so much more powerful. Awesome!
- @WhaleFell made cybermod ensure that the from_user is not null before trying to get its id, fixing an annoying frequent error. Well done!
- The project structure has been completely refactored. Now it's more organized and a lot easier to maintain.
cybermod/
├── __init__.py
├── helpers
│  ├── helpers.py
│  └── __init__.py
├── listen
│  ├── __init__.py
│  └── listen.py (used to contain Client, Message, Chat, User, MessageHandler, CallbackQueryHandler, ListenerStopped, ListenerTimeout and ListenerTypes)
├── nav
│  ├── __init__.py
│  └── pagination.py
└── utils
    ├── __init__.py
    └── utils.py (used to contain CybermodConfig and the functions patch and patchable)

Now it has the following structure:
cybermod/
├── __init__.py
├── config
│  └── __init__.py (contains the config object, formerly cybergramConfig)
├── exceptions
│  ├── __init__.py
│  ├── listener_stopped.py
│  └── listener_timeout.py
├── helpers
│  ├── __init__.py
│  └── helpers.py
├── listen
│  ├── __init__.py
│  ├── callback_query_handler.py
│  ├── chat.py
│  ├── client.py
│  ├── message_handler.py
│  ├── message.py
│  └── user.py
├── nav
│  ├── __init__.py
│  └── pagination.py
├── types
│  ├── __init__.py
│  ├── identifier.py
│  ├── listener.py
│  └── listener_types.py
└── utils
    ├── __init__.py
    └── patch.py (now contains the functions patch_into and should_patch)
- Now cybermod has documentation! You can access it at https://cybermod.pauxis.dev

There is much more for this release! Make sure to check the full release notes at
"""
