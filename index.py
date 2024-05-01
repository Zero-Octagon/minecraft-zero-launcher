import tqdm
import i18n
from utils import fi, clear_console
import config

clear_console()

print(i18n.language['welcome'])
print(fi(i18n.language['version'], {'version':config.VERSION}))