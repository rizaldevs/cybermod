## Initializing cybermod

To initialize cybermod, on the file that creates the client instance, simply import the Client class from cybermod instead
of cybergram:

```python
from cybermod import Client
```

And that's all! You can still use the `Client` class as you would normally do with cybergram, but now having all the
extra features.

>You don't need to change the imports on the plugins files. Even by importing `Client` from cybergram, the cybermod  features will be available anyway.

>In order to monkeyatch cybermod features successfully, it's just required that the  first `Client` class imported to your project code should be from cybermod. Then all the other future `Client` instances  will be patched automatically.

>On custom plugins, you just need to import Client from cybermod if you want your IDE to recognize and suggest
the extra features based on `cybermod.Client` type.
