import csv

songs = [
    [
        "DISCO ROLLING",
        "BRABANCONNE, LA",
        "BIEREN VAN BRUSSEL, DE",
        "BRUSSEL, G'ET MAAIN ÈT GESTOULE",
        "SMIDJE, 'T",
        "JAN KLAASSEN WAS TROMPETTER",
        "JEROME",
        "KRAMBAMBOULI",
        "LIEDJE VOOR LEEN",
        "ROLDERS IN DE NACHT, DE",
        "NIEMAND VERSLAAT DE SAINT-V",
        "BOERENKERMIS",
        "NOOIT STERFT HET STUDENTENRAS",
        "GILDE VIERT, DE",
        "PIETER BREUGHEL IN BRUSSEL",
        "PINNE MOUCHKE",
        "ROSEMARIE",
        "RUE DE BOUCHERS",
        "TOEN IK IN BRUSSEL KWAM",
        "VERBROEDERING TE BRUSSEL",
        "BEIAARDLIED",
        "KOEKOEKSLIED, HET",
        "WAAR HET HART VAN VOL IS, LOOPT DE MOND VAN OVER",
        "DOCHTER VAN DE PACHTER DE",
    ],
    [
        "BANDAIS-TU?",
        "ALOHA",
        "BIÈRE, LA",
        "BONNE BIÈRE BRUXELLOISE, LA",
        "CHANT DES BRAVES GUEUX",
        "CEINTURE, LA",
        "FILLES DE LA ROCHELLE, LES",
        "BOUDINS ET TEQUILA",
        "BRUXELLES",
        "C'ÉTAIT AU TEMPS QUE BRUXELLES GUINDAILLAIT",
        "DIRK FRIMOUT",
        "GILDE HALEWYN",
        "JE CHERCHE FORTUNE",
        "JE VENDS DE CARICOLES",
        "MANNEKEN PIS",
        "MARCHE DES ÉTUDIANTS, LA",
        "CHANTONS POUR PASSER LE TEMPS",
        "PARLONS BRUXELLOIS",
        "ROGER",
        "VIVRE POUR VIVRE",
        "WOLTJE ZIEVEREIR",
    ],
    [
        "BIER HER",
        "'S GIBT KEIN SCHÖNER LEBEN ALS STUDENTENLEBEN",
        "EINE SEEFAHRT",
        "KURFURST FRIEDRICH VON DER PFALZ",
        "LILI MARLEEN",
    ],
    [
        "RED RIVER VALLEY",
        "COCKLES AND MUSSELS",
        "HOME ON THE RANGE",
        "STONECUTTERS SONG, THE",
        "TOM DOOLEY",
    ],
    ["A, A, A, VALETE STUDIA", "FILIA PASTORIS", "GERTJIE", "STUDENTELIED"],
]

sorted_songs = []
for song in songs:
    sorted_songs.append(sorted(song, key=str.lower))

with open("sorted-songs.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    for lang in sorted_songs:
        for song in lang:
            writer.writerow([song])


print("Sorted songs and wrote order to 'sorted-songs.csv'")
