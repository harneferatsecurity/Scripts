# LIVRO TESTE DE PENETRAÇÃO - CAPITULO 3
# OBJETIVO: SCANNER DE PORTAS COM PERL

#! /usr/bin/perl

use strict;
use warnings;

#IMPORTA BIBLIOTECA
use IO::Socket::INET;

# USUARIO INFORMA A PORTA
print "Port: ";
my $port = <STDIN>;

# FUNÇÃO REMOVE PULA LINHA
chomp($port);

# USUARIO INFORMA IP
print "IP: ";
my $ip = <STDIN>;
chomp($ip);

# ESTABELECE A VARIAVEL DO TIPO SOCKET E VERIFICA SE A CONEXÃO TEVE SUCESSO
my $s = IO::Socket::INET->new(
	PeerHost => $ip,
	PeerPort => $port,
	Proto	=> 'tcp',

# SE A CONEXÃO FALHAR, PORTA TA FECHADA
) or die "Porta $port fechada!\n";

#SE A CONEXÃO EFETIVAR, PORTA ESTÁ ABERTA
print "Porta $port aberta!\n";

# ENCERRA CONEXÃO
$s->close();
