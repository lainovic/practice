class KeyNotFoundError(RuntimeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class HashMap:
    class Entry:
        def __init__(self, key, val) -> None:
            self.key = key
            self.val = val
            self.next = None

    def __init__(self) -> None:
        self.size = 100
        self.entries = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def _get_entry(self, key):
        entry = self.entries[self._hash(key)]
        while entry is not None:
            if entry.key == key:
                return entry
            entry = entry.next
        return None

    def put(self, key, value):
        entry = self._get_entry(key)
        if entry is not None:
            print(
                f"-----> [DEBUG][CREATE/UPDATE] Updated the existing entry ({key}, {entry.val}) with value {value}.")
            entry.val = value
            return
        idx = self._hash(key)
        if self.entries[idx] is None:
            print(
                f"-----> [DEBUG][CREATE/UPDATE] Created a new entry ({key}, {value}) at index {idx}.")
            self.entries[idx] = self.Entry(key, value)
            return
        entry = self.entries[idx]
        while entry.next is not None:
            entry = entry.next
        entry.next = self.Entry(key, value)
        print(
            f"-----> [DEBUG][CREATE/UPDATE] Created a new entry ({key}, {value}) and appended it to the existing entry at index {idx}.")

    def get(self, key):
        entry = self._get_entry(key)
        if entry is None:
            raise KeyNotFoundError(f"-----> [DEBUG][GET] Key {key} not found.")
        print(
            f"-----> [DEBUG][GET] Key {key} found -> {entry.val}.")
        return entry.val

    def contains(self, key):
        return True if self._get_entry(key) is not None else False

    def remove(self, key):
        idx = self._hash(key)
        entry = self.entries[idx]
        prev = None
        while entry is not None:
            if entry.key == key:
                print(
                    f"-----> [DEBUG][REMOVE] Key {key} found at index {idx}. Remove: {entry.val}.")
                if prev is not None:
                    prev.next = entry.next
                else:
                    self.entries[idx] = self.entries[idx].next
                return
            prev = entry
            entry = entry.next
        print(f"-----> [DEBUG][REMOVE] Key {key} not found.")
