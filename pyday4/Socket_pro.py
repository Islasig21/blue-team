import socket

def tcp_head(host,port=80,path="/"):
    req = f"HEAD {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    with socket.socket(socket.AF_INET, socket,SOCK)