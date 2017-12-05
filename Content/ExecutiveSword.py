from threading import Thread
from Content.Data import Service
from Log.Logger import Logger
from Tools.LamdbaChain import LamdbaChain
from Config import *
import time


class ExecutiveSword:
    def __init__(self):
        self.logger = Logger("ExecutiveSword")
        self.services = {}
        self.services[APP_NAME] = [Service(HIKARI_SERVER,
                                           HIKARI_VERSION,
                                           APP_NAME,
                                           LOCALHOST,
                                           HIKARI_PORT)]
        self.logger.info("add self done.".format(name=APP_NAME))
        self.killed_list = {}

        Thread(target=self.killall).start()

    def add(self, service):
        if isinstance(service, Service):
            if self.services.get(service.name, -1) == -1:
                self.services[service.name] = [service]
            else:
                if LamdbaChain(self.services[service.name]).filter(lambda x: str(x) == str(service)).len() == 1:
                    self.logger.debug("exist but += "+str(KILL_EVENT_VALUE)+"\t"+str(self.killed_list[str(service)]))
                    self.killed_list[str(service)] += KILL_EVENT_VALUE
                    return
                self.services[service.name].append(service)

            if self.killed_list.get(str(service), -1) == -1:
                self.killed_list[str(service)] = KILL_INITIAL_VALUE
                self.logger.debug(str(service) + "\t" + str(self.killed_list[str(service)]))
                self.logger.info("add {name} done.".format(name=service.name))
        else:
            pass
            self.logger.error("add {name} error.".format(name=service.name))

    def delete(self, s):
        name = s.split("://")[0]
        services = self.services.get(name, -1)
        if services != -1:
            ls = LamdbaChain(services).filter(lambda x: str(x) == s)
            if (ls.len() != 0):
                services.remove(ls.done()[0])
                self.logger.info("del {s} done.".format(s=s))
            else:
                pass

            if len(services) == 0:
                self.services.pop(name, -1)
        else:
            pass

    def killall(self):
        time.sleep(KILL_INTERVAL)
        for k, v in self.killed_list.items():
            self.killed_list[k] -= KILL_EVENT_VALUE
            self.logger.debug(k + "\t" + str(v))
        lc = LamdbaChain(self.killed_list.keys()).filter(lambda x: self.killed_list[x] <= 0)
        lc.map(lambda x: self.delete(x))
        lc.map(lambda x: self.killed_list.pop(x, -1))

        self.killall()

    def get(self, name):
        services = self.services.get(name, -1)
        if services != -1:
            return services
        else:
            return []

    def clear(self):
        self.__init__()
        self.logger.info("clear done.")


if __name__ == "__main__":
    es = ExecutiveSword()
    s = Service("HiKaRi_Server", -0.01, "mmm", "127.0.0.1", 5494)
    es.add(s)
    es.add(s)
    es.add(s)
    es.add(s)

    print(LamdbaChain(es.get("mmm")).map(lambda x: str(x)).done())
    es.delete(str(s))
    print(es.get("mmm"))
