""" create list of names with UUID"""
import uuid
given_names = ("Aalia", "Pawel", "Mysha", "Hamish", "Marco", "Jeremiah", "Gianluca", "Callen")
surnames = ("Horn", "Bartlett", "Spooner", "Jacobs", "Smyth", "Maja", "Santana")
shooters = []
for i in range(len(surnames)):
  shooters.append((uuid.uuid4(), given_names[i], surnames[i]))

print(shooters)
