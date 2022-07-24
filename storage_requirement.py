# Memory requirement (eg birth date)

world_population = 7.9e9 # Wikipedia contributors. (2022, July 23). World population. In Wikipedia, The Free Encyclopedia. Retrieved 11:17, July 24, 2022, from https://en.wikipedia.org/w/index.php?title=World_population&oldid=1100013068

import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

foo = "[08/11/1982],"
print(f"* Array mit Format: {len(foo)} byte/Eintrag. Datenbank mit {'{:.2e}'.format(world_population)} Einträgen: {convert_size(len(foo) * world_population)}.")
foo = "[08111982],"
print(f"* Array ohne Format: {len(foo)} byte/Eintrag Datenbank mit {'{:.2e}'.format(world_population)} Einträgen: {convert_size(len(foo) * world_population)}.")
foo = "08111982"
print(f"* durchgehende Wurst: {len(foo)} byte/Eintrag Datenbank mit {'{:.2e}'.format(world_population)} Einträgen: {convert_size(len(foo) * world_population)}.")
print(f"* Je ein Byte für Tag und Monat und 2 Byte für das Jahr: 4 byte/Eintrag. Datenbank mit {'{:.2e}'.format(world_population)} Einträgen: {convert_size(4 * world_population)}.\nIm Jahr 65536 bräuchte man ein weiteres Byte.")
print(f"* Festlegung Stichtag (zB 1.1.0000) und Speicherung des Geburtsdatums als Integer welche zum Stichtag hinzugezählt wird: 3 byte/Eintrag\nDatenbank mit {'{:.2e}'.format(world_population)} Einträgen: {convert_size(3 * world_population)} byte.\nIm Jahr 45935 bräuchte man ein weiteres Byte.")
foo = "01000 1011 11110111110"
print(f"* theoretischer Wert wenn man bitwise speichern könnte: {5 + 4 + 11} bit={(5 + 4 + 11) / 8} byte/Eintrag .\nDatenbank mit {'{:.2e}'.format(world_population)} Einträgen: {convert_size((5 + 4 + 11) * world_population / 8)}.\n(ab 2048 bräuchte man für das Jahre ein weiteres bit/Eintrag)")

# Proof of concept für variante 3 byte/Eintrag.
test = b"\x08\x0b\x52" * 1024 * 1024 # Byteobject with 3 bytes (this safes ~20% storage compared to strings)
with open("test9.txt", "wb") as file: # byte-write to file
  file.write(test)

foo = hex(int(2022 - 31) * 365.2425 ) # geburtsdatum des medianen Menschen. Dieses Verfahren ist ungenau daher nicht brauchbar.
import re
raggy = re.compile(r"x")
foo = raggy.sub("", foo) # "x" entfernen, da es eine Umwandlung verhindert
bar = bytes.fromhex(foo) * 1024
with open("byte_test.txt", "wb") as file:
  file.write(bar)
