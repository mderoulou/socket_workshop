void setAdress(struct sockaddr_in *adrr, unsigned long ip, int port)
{
    int addrlen = sizeof(struct sockaddr_in);
    adrr->sin_family = AF_INET;
    adrr->sin_addr.s_addr = ip;
    adrr->sin_port = htons(port);
}

int sendall(int fd, char *data, int size)
{
    while (size > 0) {
        int sendedsize = write(fd, data, size);
        if (sendedsize < 0) {
            perror("sendall failed");
            return 0;
        }
        size -= sendedsize;
        data += sendedsize;
    }
    return 1;
}

int sendstr(int fd, char *str)
{
    sendall(fd, str, strlen(str));
}

int binded_socket(int port)
{
    int server_fd;
    int opt = 1;

    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
        perror("socket failed"), exit(84);
    if (setsockopt(server_fd, 1, 2 | 15, &opt, sizeof(opt))) {
        perror("setsockopt");
        exit(84);
    }
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(port);
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0){
        perror("bind failed");
        exit(84);
    }
    listen(server_fd, 64);
    return server_fd;
}