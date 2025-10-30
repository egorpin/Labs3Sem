# test_wrapper.py
import pytest
from unittest.mock import Mock, patch, MagicMock
from wrapper import (
    LocalFileSystem,
    RemoteFileSystem,
    SourceLocalFileSystem,
    SourceRemoteFileSystem,
    FileServer,
    ISource
)

class TestLocalFileSystem:
    def test_local_read(self):
        lfs = LocalFileSystem()
        result = lfs.local_read()
        assert result == 'читаю файл на локальном устройстве...'

    def test_local_write(self):
        lfs = LocalFileSystem()
        result = lfs.local_write()
        assert result == 'записываю в файл на локальном устройстве...'

class TestRemoteFileSystem:
    def test_remote_filesystem_initialization(self):
        rfs = RemoteFileSystem('127.0.0.1')
        assert rfs.host == '127.0.0.1'

    def test_connect(self):
        rfs = RemoteFileSystem('127.0.0.1')
        result = rfs.connect()
        assert result == 'подключаюсь к удалённому устройству...'

    def test_remote_read(self):
        rfs = RemoteFileSystem('127.0.0.1')
        result = rfs.remote_read()
        assert result == 'читаю файл на удалённом устройстве...'

    def test_remote_write(self):
        rfs = RemoteFileSystem('127.0.0.1')
        result = rfs.remote_write()
        assert result == 'записываю в файл на удалённом устройстве...'

class TestSourceLocalFileSystem:
    def test_source_local_read(self):
        source = SourceLocalFileSystem()
        result = source.read()
        assert result == 'читаю файл на локальном устройстве...'

    def test_source_local_write(self):
        source = SourceLocalFileSystem()
        result = source.write()
        assert result == 'записываю в файл на локальном устройстве...'

class TestSourceRemoteFileSystem:
    def test_source_remote_read(self):
        source = SourceRemoteFileSystem('127.0.0.1')
        result = source.read()
        expected = 'подключаюсь к удалённому устройству...\nчитаю файл на удалённом устройстве...'
        assert result == expected

    def test_source_remote_write(self):
        source = SourceRemoteFileSystem('127.0.0.1')
        result = source.write()
        expected = 'подключаюсь к удалённому устройству...\nзаписываю в файл на удалённом устройстве...'
        assert result == expected

class TestFileServer:
    def test_fileserver_initialization(self):
        mock_source = Mock(spec=ISource)
        server = FileServer(mock_source)
        assert server.source == mock_source

    def test_fileserver_read_with_mock(self):
        mock_source = Mock(spec=ISource)
        mock_source.read.return_value = 'mock read result'

        server = FileServer(mock_source)
        result = server.read()

        assert result == 'mock read result'

    def test_fileserver_write_with_mock(self):
        mock_source = Mock(spec=ISource)
        mock_source.write.return_value = 'mock write result'

        server = FileServer(mock_source)
        result = server.write()

        assert result == 'mock write result'

    def test_fileserver_with_local_source(self):
        local_source = SourceLocalFileSystem()
        server = FileServer(local_source)

        read_result = server.read()
        write_result = server.write()

        assert read_result == 'читаю файл на локальном устройстве...'
        assert write_result == 'записываю в файл на локальном устройстве...'

    def test_fileserver_with_remote_source(self):
        remote_source = SourceRemoteFileSystem('127.0.0.1')
        server = FileServer(remote_source)

        read_result = server.read()
        write_result = server.write()

        expected_read = 'подключаюсь к удалённому устройству...\nчитаю файл на удалённом устройстве...'
        expected_write = 'подключаюсь к удалённому устройству...\nзаписываю в файл на удалённом устройстве...'

        assert read_result == expected_read
        assert write_result == expected_write

    @patch('wrapper.SourceLocalFileSystem')
    def test_fileserver_with_patched_local_source(self, mock_local_class):
        mock_source = Mock()
        mock_source.read.return_value = 'patched local read'
        mock_source.write.return_value = 'patched local write'
        mock_local_class.return_value = mock_source

        server = FileServer(mock_local_class())

        assert server.read() == 'patched local read'
        assert server.write() == 'patched local write'

    @patch('wrapper.SourceRemoteFileSystem')
    def test_fileserver_with_patched_remote_source(self, mock_remote_class):
        mock_source = Mock()
        mock_source.read.return_value = 'patched remote read'
        mock_source.write.return_value = 'patched remote write'
        mock_remote_class.return_value = mock_source

        server = FileServer(mock_remote_class('127.0.0.1'))

        assert server.read() == 'patched remote read'
        assert server.write() == 'patched remote write'

    def test_fileserver_dependency_injection(self):
        mock_source = MagicMock()
        mock_source.read.return_value = "читаю из mock источника"
        mock_source.write.return_value = "пишу в mock источник"

        server = FileServer(mock_source)

        assert server.read() == "читаю из mock источника"
        assert server.write() == "пишу в mock источник"

        mock_source.read.assert_called_once()
        mock_source.write.assert_called_once()

    def test_fileserver_with_different_mock_behaviors(self):
        """Тестирование FileServer с разным поведением mock объектов"""
        # Mock с разными возвращаемыми значениями для последовательных вызовов
        mock_source = Mock()
        mock_source.read.side_effect = ['first read', 'second read']
        mock_source.write.side_effect = ['first write', 'second write']

        server = FileServer(mock_source)

        assert server.read() == 'first read'
        assert server.write() == 'first write'
        assert server.read() == 'second read'
        assert server.write() == 'second write'

        assert mock_source.read.call_count == 2
        assert mock_source.write.call_count == 2

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
