function emotiv_disconnect()
    global TCP_CONNECTION
    fclose(TCP_CONNECTION);
    delete(TCP_CONNECTION);
    clear TCP_CONNECTION
end