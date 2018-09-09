#      |    |
#   11 | 21 | 31
# -----+----+-----
#   12 | 22 | 32
# -----+----+-----
#   13 | 23 | 33
#      |    |


def zahteve(indeks, pozicije, znak):
    stevec = [0, 0, 0, 0]
    for pozicija in pozicije[znak]:
        if pozicija[0] == indeks[0]:
            stevec[0] += 1
        if pozicija[1] == indeks[1]:
            stevec[1] += 1
        if pozicija[0] == pozicija[1]:
            stevec[2] += 1
        if int(pozicija[0]) + int(pozicija[1]) == 4:
            stevec[3] += 1
        if any(vsota == 3 for vsota in stevec):
            return True
