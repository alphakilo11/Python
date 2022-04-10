# money payed to russia since 24feb2022 (Beginn der Invasion der Ukraine)
import datetime

angriffsbeginn_utc = datetime.datetime(2022, 2, 24, 2, 00)
date_statement_josep_borrell = datetime.datetime(2022, 4, 6)
amount_josep_borrell = 35e9

print(angriffsbeginn_utc.strftime("%H:%M:%S %d.%m.%Y"))
dauer = datetime.datetime.today() - angriffsbeginn_utc
dauer_angriffsbeginn_statement = date_statement_josep_borrell - angriffsbeginn_utc
amount_per_day = amount_josep_borrell / dauer_angriffsbeginn_statement.days
print(f"Zeit seit Angriffsbeginn: {dauer}")
print(f"Zeit von Angriffsbeginn bis Statement: {dauer_angriffsbeginn_statement}")
print(f"Tägliche Zahlungen der EU an Russland: {amount_per_day}")