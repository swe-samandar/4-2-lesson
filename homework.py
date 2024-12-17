from random import randint
from colorama import init, Fore
import os
os.system("clear")

init(autoreset=True)
 
def random_array(n):
    return [randint(-10, 10) for _ in range(n)]


""" Series30 -> n, k natural sonlari va n ta butun sondan iborat k ta to'plam berilgan. 
Har bir to'plam uchun elementlari yig'indisini chiqaruvchi programma tuzilsin."""
def func30(n, k):
    lst = [random_array(n) for _ in range(k)]
    print(lst)
    for arr in lst:
        print(Fore.CYAN + f"{sum(arr)}")


""" Series31 -> n, k natural sonlari va n ta butun sondan iborat k ta to'plam berilgan. 
2 soni bor bo'lgan to'plamlar sonini chiqaruvchi programma tuzilsin."""
def func31(n, k):
    lst = [random_array(n) for _ in range(k)]
    for arr in lst:
        if 2 in arr:
            print(Fore.GREEN + f"{arr}")


""" Series32 -> n, k natural sonlari va n ta butun sondan iborat k ta to'plam berilgan. 
Har bir to'plamdagi birinchi uchragan 2 soni turgan nomerni chiqaruvchi programma tuzilsin. 
Agar to'plamda 2 soni bo'lmasa, 0 chiqarilsin."""
def func32(n, k):
    lst = [random_array(n) for _ in range(k)]
    print(lst)
    for arr in lst:
        if 2 in arr:
            print(Fore.GREEN + f"{arr.index(2)}")
        else:
            print(Fore.RED + f"{0}")


""" Series33 -> n, k natural sonlari va n ta butun sondan iborat k ta to'plam berilgan. 
Har bir to'plamdagi oxirgi 2 soni turgan nomerni chiqaruvchi programma tuzilsin. 
Agar 2 soni to'plamda bo'lmasa, 0 chiqarilsin."""
def func33(n, k):
    lst = [random_array(n) for _ in range(k)]
    print(lst)
    for arr in lst:
        if 2 in arr:
            print(Fore.GREEN + f"{len(arr) - 1 - arr[::-1].index(2)}")
        else:
            print(Fore.RED + f"{0}")


""" Series34 -> n, k natural sonlari va n ta butun sondan iborat k ta to'plam berilgan. 
Har bir to'plam uchun quyidagi vazifa bajarilsin. Agar to'plamda 2 soni bo'lsa, to'plam elementlari yig'indisi chiqarilsin,
aks holda 0 chiqaruvchi programma tuzilsin."""
def func34(n, k):
    lst = [random_array(n) for _ in range(k)]
    print(lst)
    for arr in lst:
        if 2 in arr:
            print(Fore.GREEN + f"{sum(arr)}")
        else:
            print(Fore.RED + f"{0}")


""" Series35 -> k natural soni va k ta to'plam berilgan. Har bir to'plam elementlarini kiritish 0 bilan tugatiladi.
Har bir to'plam uchun elementlar sonini chiqaruvchi programma tuzilsin."""
def func35(k):
    lst = [random_array(randint(1, 20)) for _ in range(k)]
    for arr in lst:
        arr.append(0)
    print(lst)
    for arr in lst: 
        print(Fore.CYAN + f"{len(arr)}")


""" Series36 -> k natural soni va k ta to'plam berilgan. Har bir to'plam elementlarini kiritish 0 bilan tugatiladi.
Har bir to'plam kamida 2 ta elementga ega. Elementlari o'suvchi bo'lgan to'plamlar sonini chiqaruvchi programma tuzilsin."""
def func36(k):
    lst = [random_array(6) for _ in range(k)]
    lst.append([-12, -10, -7, -5, -3, -1])
    for arr in lst:
        arr.append(0)
    print(lst)
    for arr in lst: 
        if sorted(arr) == arr:
            print(Fore.CYAN + f"{arr}")


""" Series37 -> k natural soni va k ta to'plam berilgan. Har bir to'plam elementlarini kiritish 0 bilan tugatiladi. 
Har bir to'plam kamida 2 ta elementga ega. Elementlari o'suvchi yoki kamayuvchi bo'lgan to'plamlar sonini chiqaruvchi programma tuzilsin."""
def func37(k):
    lst = [random_array(6) for _ in range(k)]
    lst.append([-12, -10, -7, -5, -3, -1])
    lst.append([12, 10, 7, 5, 3, 1])
    for arr in lst:
        arr.append(0)
    print(lst)
    counter = 0
    for arr in lst: 
        if sorted(arr) == arr or sorted(arr, reverse=True) == arr:
            counter += 1        
    print(Fore.CYAN + f"{counter} ta")


""" Series38 -> k natural soni va k ta to'plam berilgan. Har bir to'plam elementlarini kiritish 0 bilan tugatiladi. 
Har bir to'plam kamida 2 ta elementga ega. Har bir to'plam uchun quyidagi vazifalar bajarilsin: Agar to'plam elementlari 
o'suvchi bo'lsa 1; kamayuvchi bo'lsa -1; o'suvchi ham kamayuvchi ham bo'lmasa 0 chiqaruvchi programma tuzilsin."""
def func38(k):
    lst = [random_array(6) for _ in range(k)]
    lst.insert(1,[-12, -10, -7, -5, -3, -1])
    lst.insert(4, [12, 10, 7, 5, 3, 1])
    for arr in lst:
        arr.append(0)
    print(lst)
    for arr in lst: 
        if sorted(arr) == arr:
            print(Fore.CYAN + f"{1}")
        elif sorted(arr, reverse=True) == arr:
            print(Fore.CYAN + f"{-1}")
        else:
            print(Fore.CYAN + f"{0}")