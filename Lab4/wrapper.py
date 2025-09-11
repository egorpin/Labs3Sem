class LocalFileSystem:
    def local_read(self):
        return 'читаю файл на локальном устройстве...'

    def local_write(self):
        return 'записываю в файл на локальном устройстве...'

class RemoteFileSystem:
    def __init__(self, host):
        self.host = host

    def connect(self):
        return 'подключаюсь к удалённому устройству...'

    def remote_read(self):
        return 'читаю файл на удалённом устройстве...'

    def remote_write(self):
        return 'записываю в файл на удалённом устройстве...'

class ISource:
    def read(self):
        raise NotImplementedError()

    def write(self):
        raise NotImplementedError()

class SourceLocalFileSystem(ISource, LocalFileSystem):
    def read(self):
        return self.local_read()

    def write(self):
        return self.local_write()

class SourceRemoteFileSystem(ISource, RemoteFileSystem):
    def read(self):
        return f'{self.connect()}\n{self.remote_read()}'

    def write(self):
        return f'{self.connect()}\n{self.remote_write()}'


class FileServer:
    def __init__(self, source: ISource):
        self.source = source

    def read(self):
        return self.source.read()

    def write(self):
        return self.source.write()


if __name__ == '__main__':
    lfs = FileServer(SourceLocalFileSystem())
    rfs = FileServer(SourceRemoteFileSystem('127.0.0.1'))

    print(lfs.read())
    print(rfs.write())
