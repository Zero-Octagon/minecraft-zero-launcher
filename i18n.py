import os
import yaml
import config

if config.LANGUAGE == 'en':
    languagePath = os.path.join(config.currentPath, 'i18n/en.yml')
elif config.LANGUAGE == 'zh-cn':
    languagePath = os.path.join(config.currentPath, 'i18n/zh-cn.yml')
else:
    print('未知的语言选项')
    print('Unknown Language Options')

with open(languagePath, 'r', encoding='UTF-8') as file:
    language = yaml.safe_load(file)