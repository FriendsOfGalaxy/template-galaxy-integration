"""
Original example is taken from GOG Galaxy Python API documentation:
https://galaxy-integrations-python-api.readthedocs.io/en/latest/overview.html#basic-usage
"""

import sys

from galaxy.api.plugin import Plugin, create_and_run_plugin
from galaxy.api.consts import Platform


with open('manifest.json', 'r') as f:
    __version__ = json.load(f)['version']


class PluginExample(Plugin):
    def __init__(self, reader, writer, token):
        super().__init__(
            Platform.Generic, # Choose platform from available list
            __version__,
            reader,
            writer,
            token
        )

    # implement methods
    async def authenticate(self, stored_credentials=None):
        pass

def main():
    create_and_run_plugin(PluginExample, sys.argv)

# run plugin event loop
if __name__ == "__main__":
    main()