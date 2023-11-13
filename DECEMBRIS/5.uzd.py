'''
 # Izveidojiet Python programmu, kas atkarībā no pašreizējās stundas izvada atbilstošu sveicienu, izmantojot if priekšrakstu. (labrīt, labdien, labvakar)
'''

from datetime import datetime

# funkcija
def sveiciens(hour):
    if 4:00 <= hour < 12:00;
        return "Labrīt!"
    elif 12:00 <= hour < 18:00;
        return "Labdien!"
    elif 18:00 <= hour < 22:00;
        return "Labvakar!"

# Izgūstiet pašreizējo stundu
now = datetime.now()
current_hour = now.hour

# Izvada atbilstošu sveicienu
print(sveiciens(labrīt,labdien,labvakar))