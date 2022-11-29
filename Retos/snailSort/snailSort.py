array = [[1, 2, 3, 4, 1, 1],
         [12, 13, 14, 5, 1, 1],
         [11, 16, 15, 6, 1, 1],
         [10, 9, 8, 7, 1, 1],
         [10, 9, 8, 7, 1, 1],
         [10, 9, 8, 7, 1, 1]]
snail = []
long = len(array[0])
rep = 1
seguir = True
vueltas = 0

if len(array[0]) != 0:
    snail = snail + array[0 + vueltas]
    while seguir:
        print(vueltas)
        if not (long == 1 and rep == 2):
            for i in range(1 + vueltas, len(array[0]) - vueltas):
                snail.append(array[i][len(array) - 1 - vueltas])
            long = len(range(1 + vueltas, len(array[0]) + vueltas))

            if not (long == 1 and rep == 2):
                snail = snail + array[len(array) - 1 - vueltas][0 + vueltas:len(array) - 1 - vueltas][::-1]
                long = len(array[len(array) - 1 - vueltas][0 + vueltas:len(array) - 1 - vueltas])
                rep = 2

                if not (long == 1 and rep == 2):
                    for i in range(1 + vueltas, len(array[0]) - 1 + vueltas)[::-1]:
                        snail.append(array[i][0 - vueltas])
                    vueltas += 1
                    long = len(range(1 + vueltas, len(array[0]) - 1 + vueltas))
                    rep = 1

                    if not (long == 1 and rep == 2):
                        if len(array[0 + vueltas][0 + vueltas:len(array) - 1 - vueltas]) == 0:
                            snail = snail + array[0 + vueltas][0 + vueltas:len(array) - vueltas]
                        else:
                            snail = snail + array[0 + vueltas][0 + vueltas:len(array) - 1 - vueltas]
                        long = len(array[0 + vueltas][0 + vueltas:len(array) - vueltas])
                        rep = 2

                    else:
                        seguir = False
                else:
                    seguir = False
            else:
                seguir = False
        else:
            seguir = False

print(snail)
