# igralec × uporablja križce (×), igralec o pa krožce (o)
# lihe igre začenja igralec ×, sode pa igralec o

from pogoji import *
import tkinter as tk
from collections import defaultdict


def rezultat(indeks, zmaga=False, zmage=defaultdict(int)):
    if zmaga:
        zmage[indeks] += 1
    igralec = tk.Label(igralca, text='Igralec ' + indeks + ': ' + str(zmage[indeks]), font=('Courier', 15, 'bold'))
    if indeks == '×':
        igralec.grid(row=0, column=0, pady=(10, 2))
    else:
        igralec.grid(row=1, column=0, pady=(2, 20))


def nastavi():
    g11 = tk.Button(igra, text=' ', font=('Courier', 60), command=lambda: poteza(g11, '11'))
    g11.grid(row=0, column=0)
    g21 = tk.Button(igra, text=' ', font=('Courier', 60), command=lambda: poteza(g21, '21'))
    g21.grid(row=0, column=1)
    g31 = tk.Button(igra, text=' ', font=('Courier', 60), command=lambda: poteza(g31, '31'))
    g31.grid(row=0, column=2)

    g12 = tk.Button(igra, text=' ', font=('Courier', 60), command=lambda: poteza(g12, '12'))
    g12.grid(row=1, column=0)
    g22 = tk.Button(igra, text=' ', font=('Courier', 60), command=lambda: poteza(g22, '22'))
    g22.grid(row=1, column=1)
    g32 = tk.Button(igra, text=' ', font=('Courier', 60), command=lambda: poteza(g32, '32'))
    g32.grid(row=1, column=2)

    g13 = tk.Button(igra, text=' ', font=('Courier', 60), command=lambda: poteza(g13, '13'))
    g13.grid(row=2, column=0)
    g23 = tk.Button(igra, text=' ', font=('Courier', 60), command=lambda: poteza(g23, '23'))
    g23.grid(row=2, column=1)
    g33 = tk.Button(igra, text=' ', font=('Courier', 60), command=lambda: poteza(g33, '33'))
    g33.grid(row=2, column=2)


def poteza(gumb=None, indeks=None, pozicije=defaultdict(list), kvantiteta=[], blok=[], vrstnired=[], odpri=False):
    if odpri:
        blok.clear()
        vrstnired.clear() if vrstnired else vrstnired.append(1)
        return
    if blok:
        return
    if not gumb['text'] == ' ':
        return
    if not kvantiteta:
        if vrstnired:
            kvantiteta.append(0)
        kvantiteta.append(1)
    else:
        kvantiteta.append(kvantiteta[-1] + 1)
    if len(kvantiteta) % 2:
        gumb['text'] = '×'
        pozicije['×'].append(indeks)
        if zahteve(indeks, pozicije, '×'):
            kvantiteta.clear()
            pozicije.clear()
            blok.append(konecrunde('×'))
            return
    else:
        gumb['text'] = 'o'
        pozicije['o'].append(indeks)
        if zahteve(indeks, pozicije, 'o'):
            kvantiteta.clear()
            pozicije.clear()
            blok.append(konecrunde('o'))
            return
    if kvantiteta[-1] == 9:
        kvantiteta.clear()
        pozicije.clear()
        blok.append(konecrunde('n'))


def konecrunde(nacin):
    if nacin == '×':
        rezultat(nacin, True)
        izid = tk.Label(konec, text='Zmagal je igralec ×', font=('Courier', 15, 'bold'))
    elif nacin == 'o':
        rezultat(nacin, True)
        izid = tk.Label(konec, text='Zmagal je igralec o', font=('Courier', 15, 'bold'))
    else:
        izid = tk.Label(konec, text='Izenačen rezultat', font=('Courier', 15, 'bold'))
    izid.grid(row=0, column=0, pady=(20, 10))
    ponovi = tk.Button(konec, text='Ponovna igra', font=('Courier', 15, 'bold'), command=lambda: pospravi(izid, ponovi))
    ponovi.grid(row=1, column=0, pady=(10, 10))
    return True


def pospravi(izid, ponovi):
    nastavi()
    poteza(odpri=True)
    izid.grid_forget()
    ponovi.grid_forget()


okno = tk.Tk()
okno.title('Križec-krožec')
okno.geometry('500x700+10+10')

igralca = tk.Frame(okno)
igra = tk.Frame(okno)
konec = tk.Frame(okno)

rezultat('×')
rezultat('o')

nastavi()

igralca.pack()
igra.pack()
konec.pack()

okno.mainloop()
