import socket
import threading
import sys



def get_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('8.8.8.8', 80))
    local_ip = sock.getsockname()
    sock.close()
    return local_ip[0]


def main():
    global CLIENTS
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.listen(15)
    print(f"[*] IP : {IP}")
    print(f"[*] PORT : {PORT}")
    print("[*] Press Ctrl + C to exit.")

    while True:
        try:
            client, address = server.accept()
            CLIENTS[client] = address[0]
            print(f"[*] Accepted connection from {address[0]}:{address[1]}")
            connection_log = f"[*] {address[0]} JOINED."
            broadcast(CLIENTS, client, connection_log)
            client_handler = threading.Thread(target=handle_client, args=(client, address))
            client_handler.start()

        except KeyboardInterrupt:
            print("\b\b[*] Exiting...")
            print("[*] Server will not terminate until each user leaves.")
            server.close()
            sys.exit()


def handle_client(client_socket, addr):
    global CLIENTS
    with client_socket as sock:
        try:
            sock.send(whisper.encode("UTF-8"))
            sock.send(b"[*] Use ([IP]: message) to send a private message.")
            sock.send(b"\n[*] Note: Incorrect private-message syntax sends the message to everyone.\n")
        except:
            print(f"[*] Disconnected from {addr[0]}:{addr[1]}")
            connection_log = f"[*] {addr[0]} LEFT."
            broadcast(CLIENTS, client_socket, connection_log)
            del CLIENTS[client_socket]
            return
        while sock:
            try:
                sock.send(b" >> ")
            
            except:
                print(f"[*] Disconnected from {addr[0]}:{addr[1]}")
                connection_log = f"[*] {addr[0]} LEFT."
                broadcast(CLIENTS, client_socket, connection_log)
                del CLIENTS[client_socket]
                return

            request = sock.recv(1024)
            if request:
                request = request.decode("utf-8")
                message = f"[{addr[0]}]: {request.replace("\n", "")}"
                if "[" and "]:" in request:
                    private_msg(CLIENTS, request, CLIENTS[client_socket])
                else:
                    print(message)
                    broadcast(CLIENTS, client_socket, message)


def broadcast(client_sockets_list, client_socket, message):
    for sock in client_sockets_list:
        if sock != client_socket:
            message = "\b\b\b\b" + message + "\n >> "
            sock.send(message.encode("UTF-8"))


def private_msg(client_dict, message, sender):
    start_index = message.find("[")
    end_index = message.find("]:")
    ip_addr = message[start_index + 1 : end_index]
    priv_message = "\b\b\b\b" + "(PRIVATE)" + "[" + sender + "]:" + message[end_index + 2:] + " >> "
    client_list = [key for key, value in client_dict.items() if value == ip_addr]
    for x in client_list:
        x.send(priv_message.encode("UTF-8"))


if __name__== "__main__": 
    whisper = """
 ██████╗ ██╗   ██╗██████╗       ███████╗██╗  ██╗██╗   ██╗██████╗ 
██╔════╝ ██║   ██║██╔══██╗      ██╔════╝██║  ██║██║   ██║██╔══██╗
██║  ███╗██║   ██║██████╔╝█████╗███████╗███████║██║   ██║██████╔╝
██║   ██║██║   ██║██╔═══╝ ╚════╝╚════██║██╔══██║██║   ██║██╔═══╝ 
╚██████╔╝╚██████╔╝██║           ███████║██║  ██║╚██████╔╝██║     
 ╚═════╝  ╚═════╝ ╚═╝           ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     
 

[GITHUB]: https://github.com/aluminium65/Python-Projects
"""
    print(whisper)

    IP = get_ip()
    PORT = 9993
    CLIENTS = {}

    main()
