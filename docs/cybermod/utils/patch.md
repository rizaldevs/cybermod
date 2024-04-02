### *function* cybermod.utils.patch_into(target_class)

The `cybermod.utils.patch_into` decorator is a function used to facilitate monkeypatching of pyrogram classes with custom
methods from cybermod.

### *Parameters:*

- **target_class** (*Type*) - The target class or Pyrogram class to which you want to apply the patch.

### *Returns:*

A decorated class containing the patched methods. Each replaced method is now available prefixed with `old` in the
decorated class (e.g. `__init__` becomes `old__init__`).

### *function* cybermod.utils.should_patch(func)

The `cybermod.utils.should_patch` decorator is a function used to specify that a method should be patched into a target class.
It marks a method as patchable, indicating that it should be considered for monkeypatching by `cybermod.utils.patch_into`. This
decorator is used in conjunction with the `cybermod.utils.patch_into` decorator.

### *Parameters:*

- **func** (*Type*) - The method to be marked as patchable.

### *Returns:*

The same method with the `should_patch` attribute set to `True`.
