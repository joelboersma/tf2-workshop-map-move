import os
import sys
import shutil
from platform import uname, system

class InvalidArgumentsException(Exception):
    pass

class NoSuchDirectoryException(Exception):
    pass

def show_help() -> None:
    print("USAGE: python %s [--help] [steamapps_dir]" % __file__)
    print("  - \"--help\" will display this message.")
    print("  - \"steamapps_dir\" is an optional argument to specify the filepath to the SteamApps directory. If not given, the default SteamApps path for the current OS will be used.")

def validate_args(args: list[str]) -> None:
    if args == []:
        return
    elif "--help" in args:
        show_help()
        exit(0)
    elif len(args) > 1:
        raise InvalidArgumentsException('Too many arguments.')
    elif not os.path.exists(args[0]):
        raise InvalidArgumentsException('Specified SteamApps directory does not exist.')

def in_wsl() -> bool:
    return 'microsoft-standard' in uname().release

def get_user_home() -> str:
    return os.path.expanduser('~')

def get_default_steamapps_dir() -> str:
    if system() == 'Linux':
        if in_wsl():
            return '/mnt/c/Program Files (x86)/Steam/steamapps'
        return get_user_home() + '/.steam/steam/SteamApps/'
    elif system() == 'Darwin':  # MacOS
        return get_user_home() + '/Library/Application Support/Steam/SteamApps'
    elif system() == 'Windows':
        return 'C:\\Program Files (x86)\\Steam\\steamapps'
    else:
        raise OSError('Could not detect OS. Please specify an absolute path to your SteamApps directory.')

def get_steamapps_dir(args: list[str]) -> str:
    if len(args) > 0:
        return args[0]
    else:
        STEAMAPPS_DIR = get_default_steamapps_dir()
        if not os.path.exists(STEAMAPPS_DIR):
            raise NoSuchDirectoryException('Could not find SteamApps directory in its default location. Please specify an absolute path to your SteamApps directory.')
        return STEAMAPPS_DIR
    
def main():
    args = sys.argv[1:]
    try:
        validate_args(args)
    except Exception as e:
        print('ERROR: ' + e.args[0])
        show_help()
        return

    STEAMAPPS_DIR = get_steamapps_dir(args)
    TF2_WORKSHOP_DIR = STEAMAPPS_DIR + '/workshop/content/440'
    TF2_MAP_DIR = STEAMAPPS_DIR + '/common/Team Fortress 2/tf/maps'

    for root, _, files in os.walk(TF2_WORKSHOP_DIR, topdown=False):
        for name in files:
            if name.endswith('.bsp'):
                SRC = os.path.join(root, name)
                DEST = os.path.join(TF2_MAP_DIR, name)
                print('%s => %s' % (SRC, DEST))
                shutil.copy(SRC, DEST)

if __name__ == '__main__':
    main()
