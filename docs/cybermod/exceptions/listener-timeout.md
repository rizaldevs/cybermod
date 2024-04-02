### *exception* cybermod.exceptions.ListenerTimeout

The `ListenerTimeout` exception in cybermod is raised when a listener waits for a specified duration but times out
without receiving the expected event. It is thrown only if the `config.throw_exceptions` attribute is set to `True`.

* **Usage**

```python
from cybermod.exceptions import ListenerTimeout

try:
    message = await Client.listen(..., timeout=10)
except ListenerTimeout:
    print("Listener timed out")
```
