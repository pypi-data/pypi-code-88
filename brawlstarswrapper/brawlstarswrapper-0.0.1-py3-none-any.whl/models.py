import requests
import json


class Player():
    def client(playertag):
      corrected_tag = playertag.split('#')
      tag = corrected_tag[1]
      r = requests.get(url=f"https://api.brawlapi.com/v1/player/{tag}")
      jdata = r.json()
      return jdata

    def get_logo_link(full_data):
      lid = full_data['icon']['id']
      image = f"https://cdn.brawlstats.com/player-thumbnails/{lid}.png"
      return image

    def get_3v3victories(full_data):
      x3v3 = full_data['3vs3Victories']
      return x3v3

    def get_IsQualifiedChampionshipChallenge(full_data):
      res = full_data['isQualifiedFromChampionshipChallenge']
      if res == "true":
        result = True
      else:
        result = False
      return result

    def get_tag(full_data):
      return full_data["tag"]

    def get_name(full_data):
      return full_data["name"]

    def get_trophyCount(full_data):
      return full_data["trophies"]

    def get_expLevel(full_data):
      return full_data['expLevel']

    def get_expPoints(full_data):
      return full_data['expPoints']

    def get_highestTrophies(full_data):
      return full_data['highestTrophies']

    def get_powerPlayPoints(full_data):
      return full_data['powerPlayPoints']

    def get_highestPowerPlayPoints(full_data):
      return full_data['highestPowerPlayPoints']

    def get_soloVictories(full_data):
      return full_data['soloVictories']

    def get_duoVictories(full_data):
      return full_data['duoVictories']

    def get_bestRoboRumbleTime(full_data):
      return full_data['bestRoboRumbleTime']

    def get_bestTimeAsBigBrawler(full_data):
      return full_data['bestTimeAsBigBrawler']

    def get_nameColor(full_data):
      return full_data['nameColor']

    def get_club(full_data):
      if full_data['club'] == None or full_data['club'] == "":
        return "Not in a club"
      else:
        return full_data['club']

    def get_rank(trophies):
      if 0 <= trophies < 1000:
          rank = "Wooden"
          emoji = "<:Wooden:854349021727162388>"
      elif 1000 <= trophies < 2000:
          rank = "Bronze"
          emoji = "<:Bronze:854349059711172649>"
      elif 2000 <= trophies < 3000:
          rank = "Silver"
          emoji = "<:Silver:854349070167703593>"
      elif 3000 <= trophies < 4000:
          rank = "Gold"
          emoji = "<:Gold:854349139902726145>"
      elif 4000 <= trophies < 6000:
          rank = "Diamond"
          emoji = "<:Diamond:854349164582404156>"
      elif 6000 <= trophies < 8000:
          rank = "Crystal"
          emoji = "<:Crystal:854349204352401409>"
      elif 8000 <= trophies < 10000:
          rank = "Master"
          emoji = "<:Master:854349216758759434>"
      elif 10000 <= trophies:
          rank = "Star"
          emoji = "<:Star:854349232725950465>"
      return rank, emoji
