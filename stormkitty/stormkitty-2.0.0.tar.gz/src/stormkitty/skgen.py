import csv
import random
import requests

class skgen():
    
    def generate_random_deck(faction, display=False):
        portable_variables = {"max_deck_count":12, "begin_count":0, "CSV_URL":r'https://www.dropbox.com/s/acfzhdsostyd08s/cards.csv?dl=1'}
        CSV_URL = portable_variables["CSV_URL"]
        main_deck = []
        max_deck_count = portable_variables["max_deck_count"]
        begin_count = portable_variables["begin_count"]
        while begin_count != max_deck_count:
            with requests.Session() as s:
                download = s.get(CSV_URL)
                decoded_content = download.content.decode('utf-8')
                cards_url = csv.reader(decoded_content.splitlines(), delimiter=',')
                cards = list(cards_url)
                chosen_row = random.choice(list(cards))
                found_faction = str(chosen_row[3])
                if found_faction == str(faction) or found_faction == "neutral":
                    main_deck.append(chosen_row[0])
                    begin_count += 1
                    if display == True:
                        print(main_deck)
                else:
                    if display == True:
                        print("->", end="")

        return main_deck

    def kitty_to_deck(link):
        id = link.replace('https://stormbound-kitty.com/deck/', '')
        id = id.replace('/detail', '')
        CSV_URL = r'https://www.dropbox.com/s/acfzhdsostyd08s/cards.csv?dl=1'
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cards_url = csv.reader(decoded_content.splitlines(), delimiter=',')
            cards = list(cards_url)
        broken_id = [char for char in id]
        kitty_deck = []
        if broken_id[1] == 'x':
             broken_id.pop(0)
             broken_id.pop(0)
             for i in range(12):
                try:
                    broken_id[2] = int(broken_id[2])
                    id_check = str(broken_id[0]) + str(broken_id[1]) + str(broken_id[2])
                    broken_id.pop(0)
                    broken_id.pop(0)
                    broken_id.pop(0)
                except:
                    id_check = str(broken_id[0]) + str(broken_id[1])
                    broken_id.pop(0)
                    broken_id.pop(0)
                for row in cards:
                    if row[1] == id_check.upper():
                        kitty_deck.append(row[0])
        else:
            i=0
            for element in broken_id:
                i+=1
                try:
                    element = int(element)
                except:
                    broken_id.pop(i-2)

            for i in range(12):
               try:
                   broken_id[2] = int(broken_id[2])
                   id_check = str(broken_id[0]) + str(broken_id[1]) + str(broken_id[2])
                   broken_id.pop(0)
                   broken_id.pop(0)
                   broken_id.pop(0)
               except:
                   id_check = str(broken_id[0]) + str(broken_id[1])
                   broken_id.pop(0)
                   broken_id.pop(0)
               for row in cards:
                   if row[1] == id_check.upper():
                       kitty_deck.append(row[0])
        return kitty_deck
