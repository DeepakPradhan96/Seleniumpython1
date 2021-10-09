import configparser

def readConfigdata(section,key):
   cfg=configparser.ConfigParser()
   cfg.read('./ConfigurationFile/config.cfg')

   return cfg.get(section,key)


def readConfigdata1(section,key):
   cfg=configparser.ConfigParser()
   cfg.read('./ConfigurationFile/Element.cfg')

   return cfg.get(section,key)

print(readConfigdata1('locator','Register'))