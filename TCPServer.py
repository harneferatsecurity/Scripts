import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print(f"[*] Listing on {bind_ip}:{bind_port}")

# essa é a tread que irá lidar com o cliente_socket
def handle_client(client_socket):

    #print out what the client sends
    request = client_socket.recv(1024)
    
    print(f"[*] Received {request.decode('utf-8')}")

    #send back a packet
    client_socket.send(b"ACK!")
    client_socket.close()

# esse é o laço infinito que manterá o servidor escutando
while True:
    # servidor que em bloqueio, aguardando uma conexão
    client, addr = server.accept()

    print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")
    
    # os dados da conexão são parametrizados em uma noca tread
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
