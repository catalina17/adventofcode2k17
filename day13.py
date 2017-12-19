def update_scanners(scanner_pos):
    for l in scanner_pos:
        # Change direction if at either end of layer
        if scanner_pos[l][0] == depths[l] - 1:
            scanner_pos[l] = (scanner_pos[l][0], -1)
        elif scanner_pos[l][0] == 0:
            scanner_pos[l] = (scanner_pos[l][0], 1)
        # Update scanner
        scanner_pos[l] = (scanner_pos[l][0] + scanner_pos[l][1],\
                          scanner_pos[l][1])


depths = {}
scanner_pos = {}
init_scanner_pos = {}
severity = 0
max_layer = 0


if __name__ == '__main__':

    f = open("day13.txt", "r")
    for line in f.readlines():
        tokens = line.split(':')
        # Record depth of layer
        depths[int(tokens[0])] = int(tokens[1])
        max_layer = max(max_layer, int(tokens[0]))
        # And initial state of scanner in that layer
        scanner_pos[int(tokens[0])] = (0, 1)

    init_scanner_pos = dict(scanner_pos)

    # Part I
    for i in range(0, max_layer + 1):
        if i in scanner_pos:
            if scanner_pos[i][0] == 0:
                print i, depths[i]
                severity += i * depths[i]

        update_scanners(scanner_pos=scanner_pos)

    print severity

    # Part II
    delay = 0
    while True:
        delay += 1
        stop = True

        update_scanners(scanner_pos=init_scanner_pos)
        scanner_pos = dict(init_scanner_pos)

        for i in range(0, max_layer + 1):
            if i in scanner_pos:
                if scanner_pos[i][0] == 0:
                    print "Can't go through with delay of", delay
                    stop = False
                    break

            update_scanners(scanner_pos=scanner_pos)

        if stop:
            print "Delay of", delay, "successful!"
            break
