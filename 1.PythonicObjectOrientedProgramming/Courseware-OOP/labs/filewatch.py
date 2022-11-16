import os
import sys
import time


class FileWatcher:
    def __init__(self, path_of_file_to_watch):
        self.path = path_of_file_to_watch
        self._current_file_size = self.file_size()
        self.observers = set()

    def file_size(self):
        statinfo = os.stat(self.path)
        return statinfo.st_size

    def register(self, who):
        self.observers.add(who)

    def unregister(self, who):
        self.observers.discard(who)

    def dispatch(self, file_size):
        for observer in self.observers:
            observer.update(file_size)

    def run(self):
        while True:
            file_size = self.file_size()
            if file_size != self._current_file_size:
                self._current_file_size = file_size
                self.dispatch(file_size=file_size)
            time.sleep(1)

    def __call__(self):
        while True:
            self.run()


class FileObserver:
    def __init__(self, name):
        self.name = name

    def update(self, file_size):
        print(f"{self.name} noticed the file is now {file_size} bytes")


if __name__ == "__main__":
    file_to_watch = sys.argv[1]
    observer1 = FileObserver("Bob")
    observer2 = FileObserver("Stacy")
    watcher = FileWatcher(file_to_watch)
    watcher.register(observer1)
    watcher.register(observer2)
    watcher()
