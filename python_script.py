# LIVRO TESTE DE PENETRAÇÃO - CAPÍTULO 3 - PAG. 121
# OBJETIVO:  SCANNER DE PORTAS COM PYTHON

#! /usr/bin/python

# BIBLIOTECA SOCKET
import socket

# USUARIO INFORMA O ENDREÇO DO HOST
ip = input("Enter the ip: ")

# USUARIO INFORMA A PORTA
port_str = input("Enter the port: ")

# CONVERTE UMA STRING PARA INTEIRO
port = int(port_str)

# ESTABELECE VARIAVEL DO TIPO SOCKET PARA CONEXÕES IPV4/TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#VERIFICA SE O SOCKET ESTABELECE CONEXÃO COM HOST NA PORTA INFORMADA
if s.connect_ex((ip, port)):

	#RETORNO != 0, CONEXÃO FALHOU
	print ("Port", port, "is closed")
else:
	#RETORNO = 0, CONEXÃO BEM SUCEDIDA
	print ("Port", port, "is open")

s.close()
