import os
import yaml

currentPath = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(currentPath, 'config.yml')
versionPath = os.path.join(currentPath, 'VERSION')

with open(configPath, 'r', encoding='UTF-8') as cfgFile:
    config = yaml.safe_load(cfgFile)

with open(versionPath, 'r', encoding='UTF-8') as versionFile:
    VERSION = versionFile.read()

LANGUAGE = config['language']
AUTO_CHECK_UPDATE = config['auto-check-update']

