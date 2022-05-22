# TF2 Workshop Map Move

This repository contains a Python script `tf2_workshop_map_move.py` that will move TF2 maps you have downloaded via the workshop into TF2's primary maps directory.

## Requirements
The following requirements must be met for this script to work:
- Python must be installed on your machine ([download from python.org](https://www.python.org/downloads/))
- TF2 must be installed and in your `SteamApps` directory

## Usage
`python tf2_workshop_map_move.py [--help] [steamapps_dir]`
- `--help` will display a help message
- `steamapps_dir` is an optional argument to specify the filepath to the `SteamApps` directory. If not given, the default `SteamApps` path for the current OS will be used.