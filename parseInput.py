#!/usr/bin/env python
# coding=utf-8

def parse_file(file_name):

    f = open(file_name)

    numbers = f.readline().split()

    V = int(numbers[0])
    E = int(numbers[1])
    R = int(numbers[2])
    C = int(numbers[3])
    X = int(numbers[4])

    #print V, E, R, C, X

    size_videos = f.readline().split() # V numbers, one for each video (size in Mb)

    endpoints = []
    for i in range(E):
        LDK = f.readline().split()
        Ld = int(LDK[0]) # Latency of serving a video request from the data center to its endpoint
        K = int(LDK[1]) # Number of cache servers at this endpoint

        cache_servers_at_endpoint_i = []
        for j in range(K):
            CLC = f.readline().split()
            C = int(CLC[0])
            Lc = int(CLC[1])
            cache_servers_at_endpoint_i.append((C, Lc))

        endpoints.append( (Ld, K, cache_servers_at_endpoint_i) )


    return V, E, R, C, X, size_videos, endpoints

# yolo

if __name__ == '__main__':

    file_name = "Data/me_at_the_zoo.in"

    V, E, R, C, X, size_videos, endpoints = parse_file(file_name)

    print("Nb Videos:", V)
    print("Nb Endpoints:", E)
    print("Nb Request Descriptions:", R)
    print("Nb Cache Servers:", C)
    print("Capacity of each cache servers:", X)
    print("Size of each of the " + str(V) + " videos:", size_videos)

    print("")

    print("== Description of the " + str(E) + " endpoints ==")

    for i in range(E):
        print('- ' + str(endpoints[i]))
