# template-repository-structure
Unofficial template for GOG Galaxy 2.0 integrations.

Remember to change author in License file.

---

## Installation
1. Download [latest release](https://github.com/FriendsOfGalaxy/galaxy-integration-battlenet/releases) of the plugin for your platform.
2. Create plugin folder:
	- Windows: `%LOCALAPPDATA%\GOG.com\Galaxy\plugins\installed\<my-plugin-name>`
	- MacOS: `${HOME}/Library/Application Support/GOG.com/Galaxy/plugins/installed/<my-plugin-name>`
3. Unpack downloaded release to created folder.
4. Restart GOG Galaxy Client.

## Issue reporting
Along with you detailed problem description, you may need to attach plugin log files located at:
- Windows: `%programdata%\GOG.com\Galaxy\logs`
- MacOS: `/Users/Shared/GOG.com/Galaxy/Logs`

for example:
`C:\\ProgramData\GOG.com\Galaxy\logs\plugin-name-1231-f2f22-f23f2-23ff2.log`

## Development

1. create and activate virtual environment
2. install dependencies

        pip install -r requirements/dev.txt

3. run tests

        pytest
