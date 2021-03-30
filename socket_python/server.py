# 채팅 서버
# python의 twisted 패키지 : 네트워크 통신을 쉽게 구현할 수 있도록 하는 패키지

from twisted.internet import protocol, reactor
# ModuleNotFoundError: No module named 'twisted' -> pip install scrapy
# print("import complete")

# Chat 클래스에 채팅 서버의 logic 작성


class Chat(protocol.Protocol):
    def connectionMade(self):
        # print('connected')  # 사용자가 서버에 접속하면 'connected' 메시지 출력
        self.transport.write('connected'.encode())
        # 클라이언트가 연결되면 connected 메시지를 클라이언트에 전송
        # encode : 문자열 -> 바이트

    def dateReceived(self, data):
        print(data.decode('utf-8'))  # 사용자가 서버에 메시지를 보내면 실행 사용자 메시지(data) 출력

# 통신 프로토콜 정의


class ChatFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Chat()


print('Server started!')
reactor.listenTCP(8000, ChatFactory())  # TCP 8000번 포트 Listen
reactor.run()
