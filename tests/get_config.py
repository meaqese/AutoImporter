import autoimporter
from pathlib import Path
from pytest import raises


def test_main():
    config = autoimporter.get_config(Path('../sandbox/config.yaml'))
    assert config == {
        'import': ['blocks/*/**', 'blocks/*'],
        'destination': 'styles.scss'
    }


def test_file_not_found():
    with raises(FileNotFoundError):
        autoimporter.get_config(Path('../sandbox/config.ymlqqq'))
