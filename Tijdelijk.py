import re
prijzen_dictionary = {
    "aardbei" : 3,
    "vanille" : 4,
    "Chocolade" : 5
}
aanbieding = prijzen_dictionary["vanille"] **0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - Slechts € {aanbieding}."
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()
#Punt 7 in huiswerk is ondelijkdek: een list van woorden. Geen leestekens?
#Alternatieve oplossing met re
#reclame_tekst4 = re.findall(r'\b\w+\b',reclame_tekst3)
for el in reclame_tekst4:
    if len(el) <=4:
        print((el).lower())
    else: 
        print((el).upper())

