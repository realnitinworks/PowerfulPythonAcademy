import os
import sys
import time
from enum import Enum, auto, unique


@unique
class ChangeType(Enum):
    INCREASE = auto()
    DECREASE = auto()


class FileWatcher:
    def __init__(self, path_of_file_to_watch):
        self.path = path_of_file_to_watch
        self._current_file_size = self.file_size()
        self.channels = {
            ChangeType.INCREASE: {},
            ChangeType.DECREASE: {},
        }

    def file_size(self):
        statinfo = os.stat(self.path)
        return statinfo.st_size

    def register(self, change_type, who, callback):
        self.channels[change_type][who] = callback

    def unregister(self, change_type, who):
        del self.channels[change_type][who]

    def dispatch(self, change_type, file_size):
        for callback in self.channels[change_type].values():
            callback(file_size)

    def change_type(self, file_size):
        if file_size == self._current_file_size:
            return None
        return (
            ChangeType.INCREASE
            if file_size > self._current_file_size
            else ChangeType.DECREASE
        )

    def run(self):
        while True:
            time.sleep(1)
            file_size = self.file_size()
            change_type = self.change_type(file_size)
            if not change_type:
                continue
            self.dispatch(change_type, file_size=file_size)
            self._current_file_size = file_size

    def __call__(self):
        while True:
            self.run()


class FileObserver:
    def __init__(self, name):
        self.name = name

    def increase(self, file_size):
        print(f"{self.name} noticed the file increased to {file_size} bytes")

    def decrease(self, file_size):
        print(f"{self.name} noticed the file decreased to {file_size} bytes")


if __name__ == "__main__":
    file_to_watch = sys.argv[1]
    bob = FileObserver("Bob")
    stacy = FileObserver("Stacy")
    john = FileObserver("John")
    watcher = FileWatcher(file_to_watch)
    watcher.register(ChangeType.INCREASE, bob, bob.increase)
    watcher.register(ChangeType.DECREASE, stacy, stacy.decrease)
    watcher.register(ChangeType.INCREASE, john, john.increase)
    watcher.register(ChangeType.DECREASE, john, john.decrease)
    watcher()
