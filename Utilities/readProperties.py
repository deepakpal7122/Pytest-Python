import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url
    
    @staticmethod
    def getUserMobileNumber():
        mobilenumber = config.get('common info', 'mobilenumber')
        return mobilenumber
    
    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password