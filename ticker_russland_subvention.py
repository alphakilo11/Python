# money payed to russia since 24feb2022 (Beginn der Invasion der Ukraine)
# TODO create ticker effect
import datetime
import time

angriffsbeginn_utc = datetime.datetime(2022, 2, 24, 2, 00)
ab_utc = time.struct_time((2022, 2, 24, 2, 0, 0, 0, 0 ,0)) # seconds since epoch
date_statement_josep_borrell = datetime.datetime(2022, 4, 6)
amount_josep_borrell = 35e9

print("Angriffsbeginn: ", angriffsbeginn_utc.strftime("%H:%M:%S %d.%m.%Y"), "UTC")
dauer = datetime.datetime.today() - angriffsbeginn_utc
dauer_angriffsbeginn_statement = date_statement_josep_borrell - angriffsbeginn_utc
amount_per_day = amount_josep_borrell / dauer_angriffsbeginn_statement.days
print(f"Zeit seit Angriffsbeginn: {dauer}")
print(f"Zeit von Angriffsbeginn bis Statement: {dauer_angriffsbeginn_statement}")
print(f"Tägliche Zahlungen der EU an Russland: {amount_per_day}")
print(f"Zahlungen der EU an Russland seit Beginn der Invasion: € {round(amount_per_day * dauer.days)}")
print(f"Zahlungen seit Beginn der Invasion: ", end="")
while 1:
  zahlungen = round((amount_per_day / 24 / 3600) * (time.time() - calendar.timegm(ab_utc)))
  print(f"{zahlungen} €", end="")
  time.sleep(1)
  print("\b" * (len(str(zahlungen)) + 2), end="") # replace value