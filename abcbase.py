class ABClass:
    pass


class ABCError(ABClass, Exception):
    pass


class ABCMethod(ABClass):
    pass


class ABCWith(ABCMethod):
    def __enter__(self): return self
    def __exit__(self): pass


class ABCAsyncWith(ABCWith):
    async def __aenter__(self): return self
    async def __aexit__(self): pass


class ABCIterator(ABCMethod):
    def __iter__(self): return self
    def __next__(self): pass


class ABCAsyncIterator(ABCIterator):
    async def __aiter__(self): return self
    async def __anext__(self): pass


class ABCStorage(ABClass):

    class ABCStorageError(ABCError):
        pass

    def __init__(self):
        self._storage = {}

    async def add(self, key, value) -> None:
        try:
            self._storage[key] = value
        except Exception as ex:
            raise self.ABCStorageError(str(ex))

    async def delete(self, key):
        try:
            del self._storage[key]
        except Exception as ex:
            raise self.ABCStorageError(str(ex))

    async def get(self, key):
        return self._storage.get(key)

    def __eq__(self, other): return other in self._storage
