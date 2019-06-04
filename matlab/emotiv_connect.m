function emotiv_connect()
    global TCP_CONNECTION
    TCP_CONNECTION = tcpip('localhost', 38366);
    fopen(TCP_CONNECTION);
end