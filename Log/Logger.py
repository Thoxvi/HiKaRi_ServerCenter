import time
class Logger:
    def __init__(self,who):
        self.who=who

    def lv0(self,string):
        self.xjbx(string)
    def lv1(self,string):
        self.info(string)
    def lv2(self,string):
        self.warning(string)
    def lv3(self,string):
        self.error(string)


    def debug(self,string):
        self.print(string,"Debug")

    def xjbx(self,string):
        self.print(string,"Xjbx")
        pass
    def warning(self,string):
        pass
    def info(self,string):
        pass
    def error(self,string):
        pass

    def print(self,string,lv):
        data="{lv}\t{who}\t{time}\t{string}".format(lv=lv,who=self.who,time=time.time(),string=string)
        print(data)





