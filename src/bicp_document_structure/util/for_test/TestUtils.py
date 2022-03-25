import socket
import threading

import zmq


def findNewSocketPort():
    sock = socket.socket()
    sock.bind(('', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port

def startREPServer(isOk, port, zContext, onReceive):
    repSocket = zContext.socket(zmq.REP)
    repSocket.bind(f"tcp://*:{port}")

    while True:
        receive = repSocket.recv()
        if str(receive, "utf-8") == "close":
            break
        onReceive(receive)
        if isOk:
            repSocket.send("ok".encode())
        else:
            repSocket.send("fail".encode())
    repSocket.close()


def startREPServerOnThread(isOk, port, zContext, onReceive) -> threading.Thread:
    thread = threading.Thread(target = startREPServer, args = [isOk, port, zContext, onReceive])
    thread.start()
    return thread

def sendClose(_socket):
    _socket.send("close".encode())