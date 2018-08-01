# -*- coding:utf-8 -*-
import sys,os
import ConfigParser #2.7版本
#     import ConfigParser
# except ModuleNotFoundError:
#     from configparser import ConfigParser

class Configure(object):

    def __init__(self):
        self.configPath = os.path.dirname(__file__) + '/config.ini'
        if sys.version_info >= (3,3):
            self.config = ConfigParser()
            self.config.read(self.configPath,encoding="utf-8-sig")
        else:
            self.config = ConfigParser.ConfigParser()
            self.config.read(self.configPath)

    @property
    def configure(self):
        config = {}
        sections = self.config.sections()#将配置文件中所有“[ ]”读取到列表中：
        for i in sections:
            config = dict(config,**dict(self.config.items(i)))
        return config

    @configure.setter#可读可写
    def configure(self, *value):
        self.config.set(section = list(*value)[0],option = list(*value)[1],value = list(*value)[2])
        with open(self.configPath,"w+") as f:
            self.config.write(f)

    def getConfigure(self):
        return self.configure

    def setConfigure(self,section,key,value):
        self.configure = (section,key,value)

class Config(Configure):

    def __init__(self):
        super(Config,self).__init__()
        for k,v in self.getConfig.items():
            setattr(self,k,v)

    @property
    def getConfig(self):
        return self.getConfigure()

    def setConfig(self,section,key,value):
        self.setConfigure(section,key,value)



if __name__ == '__main__':
    # b = Configure()
    # b.setConfigure(section = "APP",key = "name",value = "zyzy")
    a = Config()
    # print(a.log_path)
    a.setConfig('APP','app_package','com.yonyou.merchart')
