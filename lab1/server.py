#!/usr/bin/python

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = 'localhost'
port = 12345
s.bind((host, port))


while True:
    print 'Esperando conexao'
    c, addr = s.recvfrom(4096)
    print 'Esperando mensagem'
    print 'Mensagem recebida: ', c
    print 'Digite a resposta: '
    resposta = raw_input()
    sent = s.sendto(resposta, addr)
    print 'Resposta enviada.'
    print 'Encerrando Conexao.'
    # c.close()