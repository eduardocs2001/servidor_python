#!/usr/bin/env python3

import socket

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen()
print('Aguardando a conexão de um cliente')

conn, ender = s.accept()

print('Conectado em', ender)

while True:
    data = conn.recv(1024)
    if not data:
        print('Fechando a conexão')
        conn.close()
        break

    conn.sendall(data)
