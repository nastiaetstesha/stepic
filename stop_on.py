from typing import Any


def stop_on(iterable: iter, obj: Any) -> Any:
    for item in iterable:
        if item == obj:
            break
        yield item
