
class Service:
    '''
    protocol must be "HiKaRi_Server"
    Version < 0
    name is name
    host is ip/url
    port is port
    '''

    def __init__(self, protocol, version, name, host, port):
        self.protocol = protocol
        self.version = version
        self.name = name
        self.host = host
        self.port = port

    def toDict(self):
        return self.__dict__

    def __str__(self):
        return self.name + "://" + str(self.host) + ":" + str(self.port)


class Heartbeat:
    '''
    request_time is request time
    response_time is response time
    times is times++
    '''
    times = 0

    def __init__(self, request_time, response_time, times):
        self.request_time = request_time
        self.response_time = response_time
        self.times = times


if __name__ == "__main__":
    s = Service("HiKaRi_Server", -0.01, "mmm", "127.0.0.1", 5494)
    print(s.toDict())
    print(str(s))
