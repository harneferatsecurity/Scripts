# LIVRO TESTE DE PENETRAÇÃO - CAPITULO 3
# OBJETIVO: SCANNER DE PORTAS COM RUBY

#! /usr/bin/ruby

# IMPORTA BIBLIOTECA SOCKET
require 'socket'

print "ip: "

# USUÁRIO INFORMA O IP
ip = gets.chomp

print "port: "

# USUÁRIO INFORMA A PORTA
port = gets.chomp.to_i

begin
  # TENTA ESTABELECER UMA CONEXÃO COM O IP E PORTA INFORMADOS
  s = TCPSocket.new(ip, port)
  puts "Porta #{port} aberta."
  s.close
rescue Errno::ECONNREFUSED
  # TRATA O ERRO CASO A CONEXÃO SEJA RECUSADA
  puts "Conexão recusada: Porta #{port} fechada."
rescue SocketError => e
  # TRATA O ERRO CASO O IP SEJA INVÁLIDO OU OCORRA OUTRO ERRO DE SOCKET
  puts "Erro de conexão: #{e.message}"
end

