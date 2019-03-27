#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = 'localhost'
port = 12345

print 'Digita uma mensagem:'
mensagem = raw_input()

s.connect((host, port))
s.send(mensagem)
print 'Mensagem enviada.'
print 'Esperando resposta.'
print 'Resposta recebida:', s.recv(1024)
print 'Desconectando.'
s.close()
