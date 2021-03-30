# 클라이언트 코드 작성

import socket
import select
import sys

# socket 통신 코드 작성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8000))  # 서버 접속 / 127.0.0.1 == localhost == 내 컴퓨터

# 무한루프 / 서버로부터 메시지를 기다림

while True:
    read, write, fail = select.select(
        (s, sys.stdin), (), ())  # 소켓에서 메시지를 읽을 수 있을 때까지 대기
# sys.stdin : 사용자 키보드 입력을 기다림(엔터칠 때까지)

    for desc in read:
        if desc == s:  # 만약 서버에서 온 메시지라면 : 메시지를 출력한다
            data = s.recv(4096)  # 메시지가 도착하면 소켓에서 4096바이트를 읽는다
            print(data.decode())  # 바이트 -> 문자열 출력
        else:  # 만약 사용자가 입력한 거라면:
            msg = desc.readline()  # 사용자가 입력한 문자열을 읽어서 서버에 전송한다
            s.sned(msg.encode())
