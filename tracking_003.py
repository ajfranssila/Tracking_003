import json
import matplotlib.pyplot as plt
import statistics


# -----------------------------------------------------------
# Skripti anomalioiden etsintään, joka käy JSON-muodossa olevaa dataa läpi. Joka alueen yhden päivän arvoista (200 arvoa) otetaan baseline ensimmäisestä arvosta. 
# Jos seuraava arvo on pienempi kuin baseline, lisätään sen erotus erillään olevaan muuttujaan. Jos arvo oli suurempi kuin baseline, tehdään tästä arvosta uusi baseline. 
# Yhden päivän arvot tulostetaan, jos heittoa on yli tuhat edelliseen päivään.
# -----------------------------------------------------------

with open("flood.txt", "r") as file:
        f = file.readlines()[0].encode('utf8');

json = json.loads(f);
total_regions = 0
edellinen = 0
countaulukko = []
count_edellinen = 0
korkeustaulukko = []

for region in json['regions']:
        region_id = region['regionID']
        readings = region['readings']
        for single_reading in readings:
                date = single_reading['date']
                reading_id = single_reading['readingID']
                korkeudet = single_reading['reading']
                count = 0
                baseline = korkeudet[0]
                for korkeus in range(0, len(korkeudet)):
                    korkeustaulukko.append(korkeudet[korkeus])
                    
                    if korkeudet[korkeus] < baseline:
                        count += (baseline - korkeudet[korkeus])
                    if korkeudet[korkeus] > baseline:
                        baseline = korkeudet[korkeus]

                countaulukko.append(count)

                if reading_id != "A" and ((count > count_edellinen + 1000) or (count < count_edellinen - 1000)):
                    print (region_id + "," + date + "," + reading_id + "," + str(count))

                count_edellinen = count
