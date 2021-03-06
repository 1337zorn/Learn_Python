# Modul
import re


tx = "Haus und Maus und Laus"
print(tx)

# 1: Exater Text
txneu = re.sub("Maus", "x", tx)
print("1:", txneu)

# 2: Wahl zwischen bestimmten Zeichen
txneu = re.sub("[HM]aus", "x", tx)
print("2:", txneu)

# 3: Alle Buchstaben aus Bereich
txneu = re.sub("[L-M]aus", "x", tx)
print("3:", txneu)

# 4: Alle Buchstaben nicht aus Bereich
txneu = re.sub("[^L-M]aus", "x", tx)
print("4:", txneu)

# 5: Beliebiges Zeichen
txneu = re.sub(".aus", "x", tx)
print("5:", txneu)

# 6: Suchbegriff nur am Anfang des Texts
txneu = re.sub("^.aus", "x", tx)
print("6:", txneu)

# 7: Suchbegriff nur am Ende des Texts
txneu = re.sub(".aus$", "x", tx)
print("7:", txneu)

tx = "0172-445633"
print(tx)

# 8: Alle Ziffern aus Bereich
txneu = re.sub("[0-2]", "x", tx)
print("8:", txneu)

# 9: Alle Zeichen nicht aus Ziffernbereich
txneu = re.sub("[^0-2]", "x", tx)
print("9:", txneu)

# 10: Alle Zeichen oder Ziffern, die angegeben sind
txneu = re.sub("[047-]", "x", tx)
print("10:", txneu)

tx = "aa und aba und abbaa und abbba und aca"
print(tx)

# 11: Wiederholung, beliebig oft
txneu = re.sub("ab*a", "x", tx)
print("11:", txneu)

# 12: Wiederholung, 1 oder mehr
txneu = re.sub("ab+a", "x", tx)
print("12:", txneu)

# 13: Wiederholung, 0 oder 1
txneu = re.sub("ab?a", "x", tx)
print("13:", txneu)

# 14: Wiederholung, m bis n
txneu = re.sub("ab{2,3}", "x", tx)
print("14:", txneu)

tx = "aa und aba und abba und aca und addda"
print(tx)
# 15: Wiederholung der max. Menge von Zeichen
txneu = re.sub("a.*a", "x", tx)
print("15:", txneu)

# 16: Wiederholung der min. Menge von Zeichen
txneu = re.sub("a.*?a", "x", tx)
print("16:", txneu)