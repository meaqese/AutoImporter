from pathlib import Path
from yaml import safe_load
from argparse import ArgumentParser, Namespace
from glob import glob


def get_args() -> Namespace:
    """Parse and get all args"""
    parser = ArgumentParser()
    parser.add_argument('config', type=str,
                        help='The autoimporter config filename, e.g.: config.yaml')

    return parser.parse_args()


def get_config(config_path: Path) -> dict:
    """Import and get config file"""
    with open(config_path.as_posix(), mode='r') as config_file:
        config = safe_load(config_file)

        return config


def get_paths(config_path: Path, config: dict) -> list[list]:
    """Get all paths from config_path directory"""
    dirname = config_path.parent

    paths = []
    extension = config['destination'].split('.')[-1]

    for import_path in config['import']:
        paths.append(glob((dirname / f'{import_path}{extension}').as_posix()))

    return paths


def process_paths(config_path: Path, config: dict) -> list:
    """Normalize and join all paths"""
    dirname = config_path.parent

    result = []
    for sub_paths in get_paths(config_path, config):
        result.extend([
            Path(sub_path).as_posix().replace(dirname.name + '/', '')
            for sub_path in sub_paths])

    return result


def import_files(config_path: Path, config: dict) -> None:
    """Import all paths to destination file"""
    dirname = config_path.parent
    paths = process_paths(config_path, config)

    imports = [f'@import "{path}";\n' for path in paths]

    with open(dirname / config['destination'], mode='w+') as destination:
        destination.writelines(imports)


if __name__ == '__main__':
    try:
        config_file_path = Path(get_args().config)
        config_data = get_config(config_file_path)
        import_files(config_file_path, config_data)
    except FileNotFoundError:
        print('File not found')
