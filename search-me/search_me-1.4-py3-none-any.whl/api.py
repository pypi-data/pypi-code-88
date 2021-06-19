# -*- coding: utf-8 -*-
import os
import abc
import time
import json
import random
import pickle
import pdfkit
import PyPDF2
import logging
import chardet
import textract
import requests
import langdetect
import pandas as pd
import multiprocessing as mp
from tumblpy import Tumblpy
from bs4 import BeautifulSoup
from urllib.parse import quote
from prettytable import PrettyTable
from xh1scr import TikTok as tik_tok
from facebook_scraper import get_posts
from summa import summarizer, keywords
from concurrent.futures import ThreadPoolExecutor, TimeoutError, thread as cf_thread
from snscrape.modules import vkontakte as sns_vk, telegram as sns_tg, twitter as sns_tw
# from math import ceil
# from itertools import islice
# from instaloader import Instaloader, Profile
# config = pdfkit.configuration(wkhtmltopdf='wkhtmltopdf.exe')

logger = logging.getLogger("SEARCH ME")
stream = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s ### %(name)s ### %(message)s')
stream.setFormatter(formatter)
logger.addHandler(stream)
logger.addHandler(logging.NullHandler())
__base__ = os.getcwd()
s_vk, s_ig, s_tg, s_tw, s_yt, s_fb, s_tb, s_sc, s_tk = "vk", "instagram", "telegram", "twitter", "youtube", "facebook", "tumblr", "snapchat", "tiktok"


class Search(metaclass=abc.ABCMeta):

	def __init__(
		self,
		results=10,
		retry=10,
		show_results=True,
		cache=True,
		sleep_min=0.0,
		sleep_max=1.5,
		pdf_report=False,
		pdf_timeout=30,
		pdf_threads=mp.cpu_count(),
		pdf_parse=False,
		pdf_options={
			"text": True,
			"summary": True,
			"summary_params": ("ratio", 0.15),
			"urls": True,
			"keywords": True
			},
		use_social_search=False,
		socials=(s_vk, s_ig, s_tg, s_tw, s_yt, s_fb, s_tb, s_sc, s_tk),
		social_threads=mp.cpu_count(),
		social_options={
			"posts_limit": 10,
			"export_data": True,
			"export_format": "csv",
			"download_media": True
			}):
		self.results = results
		self.retry = retry
		self.show_results = show_results
		self.cache = cache
		self.sleep_min = sleep_min
		self.sleep_max = sleep_max
		self.pdf_report = pdf_report
		self.pdf_timeout = pdf_timeout
		self.pdf_threads = pdf_threads
		self.pdf_parse = pdf_parse
		self.pdf_options = pdf_options
		self.use_social_search = use_social_search
		self.socials = socials
		self.social_threads = social_threads
		self.social_options = social_options
		self.search_results = []
		self.mapping_obj = {
			s_vk: Vk,
			s_ig: Instagram,
			s_tg: Telegram,
			s_tw: Twitter,
			s_yt: Youtube,
			s_fb: Facebook,
			s_tb: Tumblr,
			s_sc: Snapchat,
			s_tk: Tiktok
			}
		for __social, __obj in self.mapping_obj.items():
			setattr(self, __social, __obj(**self.social_options)) if __social in self.socials else setattr(self, __social, None)
		self.mapping_dir = {
			s_ig: self.instagram,
			s_yt: self.youtube,
			s_tb: self.tumblr,
			s_sc: self.snapchat
			}
		self.mapping_adr = {
			s_vk: f"{s_vk}.com",
			s_ig: f"{s_ig}.com",
			s_tg: "t.me",
			s_tw: f"{s_tw}.com",
			s_yt: f"{s_yt}.com",
			s_fb: f"{s_fb}.com",
			s_tb: f"{s_tb}.com",
			s_sc: f"{s_sc}.com",
			s_tk: f"{s_tk}.com"
			}
		self.mapping_main = {
			s_vk: self.vk,
			s_ig: self.instagram,
			s_tg: self.telegram,
			s_tw: self.twitter,
			s_yt: self.youtube,
			s_fb: self.facebook,
			s_tb: self.tumblr,
			s_sc: self.snapchat,
			s_tk: self.tiktok
			}
		logger.debug(str(self))

	def __str__(self):
		return f"""
NUMBER RESULTS → {self.results}
NUMBER RETRIES → {self.retry}
SHOW RESULTS → {self.show_results}
SLEEP RANGE → {self.sleep_min} - {self.sleep_max} s
CACHE → {self.cache}
PDF REPORT → {self.pdf_report}
PDF TIMEOUT → {self.pdf_timeout}
PDF THREADS → {self.pdf_threads}
PDF PARSE → {self.pdf_parse}
PDF OPTIONS → {self.pdf_options}
USE SOCIAL SEARCH → {self.use_social_search}
SOCIALS → {self.socials}
SOCIAL THREADS → {self.social_threads}
SOCIAL OPTIONS → {self.social_options}"""

	@abc.abstractmethod
	def search(self):
		pass

	def show(self):
		table = PrettyTable()
		table.field_names = ["RATING", "RESULT"]
		table.align["RESULT"] = "l"
		for result in self.search_results:
			table.add_row(["🔎", result["item"]])
			for rating, link in enumerate(result["links"]):
				table.add_row([rating + 1, link])
		print(table)

	@staticmethod
	def export(item, link, k):
		__pdf_path = os.path.join(__base__, item, f"{str(k)} — {link.split('/')[2]}.pdf")
		try:
			pdfkit.from_url(link, __pdf_path)
		except Exception as e:
			logger.debug(f"EXPORT PDF EXCEPTION {k} {link} → {str(e)}")
		finally:
			return __pdf_path

	def pdf_reports(self):
		for result in self.search_results:
				with ThreadPoolExecutor(max_workers=self.pdf_threads) as executor:
					for count, link in enumerate(result["links"]):
						try:
							_path = executor.submit(
								self.export,
								link=link,
								item=result["item"],
								k=count
								).result(timeout=self.pdf_timeout)
						except TimeoutError as e:
							logger.debug(f"EXPORT PDF TIMEOUT EXCEPTION {count} {link} → {str(e)}")
						else:
							if self.pdf_parse:
								if not("pdf" in result):
									result["pdf"] = []
								if os.path.exists(_path):
									_pdf = {}
									self.pdf = PDF(
										path=_path,
										summary_params=self.pdf_options["summary_params"]
										)
									_pdf["path"] = _path
									for fld in ["text", "summary", "urls", "keywords"]:
										if self.pdf_options[fld]:
											_pdf[fld] = getattr(self.pdf, fld)
									result["pdf"].append(_pdf)
					executor.shutdown(wait=False)
					executor._threads.clear()
					cf_thread._threads_queues.clear()

	def cache_pkl(self, path="tmp.pkl"):
		with open(path, "wb") as pkl:
			pickle.dump(self.search_results, pkl)

	def cache_json(self, path="tmp.json"):
		with open(path, "w") as js:
			json.dump(self.search_results, js, indent=5, ensure_ascii=True)

	@staticmethod
	def makedirs(items):
		for item in items:
			os.makedirs(os.path.join(__base__, item), exist_ok=True, mode=0o777)

	def use_social(self):
		for searched_item in self.search_results:
			searched_item["socials"] = {}
			for __social, __social_obj in self.mapping_dir.items():
				if not(__social_obj is None):
					os.makedirs(
						os.path.join(__base__, searched_item["item"], __social),
						exist_ok=True,
						mode=0o777
						)
			with ThreadPoolExecutor(max_workers=self.social_threads) as executor:
				for link in searched_item["links"]:
					__domain = link.split("/")[2]
					for __social, __social_obj in self.mapping_main.items():
						if (
							(self.mapping_adr[__social] in __domain) and
							not(__social_obj is None)
						):
							searched_item["socials"][__social] = executor.submit(__social_obj.search, link=link, searched_item=searched_item["item"]).result()
						else:
							continue


class Google(Search):

	domains = (
		'com', 'al', 'dz', 'as', 'ad', 'am', 'ac', 'at', 'az', 'bs', 'by', 'be',
		'bj', 'ba', 'vg', 'bg', 'bf', 'cm', 'ca', 'cv', 'cat', 'cf', 'td', 'cl',
		'cn', 'cd', 'cg', 'ci', 'hr', 'cz', 'dk', 'dj', 'dm', 'tl', 'ec', 'ee',
		'fm', 'fi', 'fr', 'ga', 'gm', 'ps', 'ge', 'de', 'gr', 'gl', 'gp', 'gg',
		'gy', 'ht', 'hn', 'hu', 'is', 'iq', 'ie', 'im', 'it', 'jp', 'je', 'jo',
		'kz', 'ki', 'kg', 'la', 'lv', 'li', 'lt', 'lu', 'mk', 'mg', 'mw', 'mv',
		'ml', 'mu', 'md', 'mn', 'me', 'ms', 'nr', 'nl', 'ne', 'ng', 'nu', 'no',
		'ps', 'pn', 'pl', 'pt', 'ro', 'ru', 'rw', 'sh', 'ws', 'sm', 'st', 'sn',
		'rs', 'sc', 'sk', 'si', 'so', 'es', 'lk', 'sr', 'ch', 'tg', 'tk', 'to',
		'tt', 'tn', 'tm', 'ae', 'vu'
		)

	languages = (
		'af', 'ach', 'ak', 'am', 'ar', 'az', 'be', 'bem', 'bg', 'bh', 'bn', 'br',
		'bs', 'ca', 'chr', 'ckb', 'co', 'crs', 'cs', 'cy', 'da', 'de', 'ee','el',
		'en', 'eo', 'es', 'es-419', 'et', 'eu', 'fa', 'fi', 'fo', 'fr', 'fy',
		'ga', 'gaa', 'gd', 'gl', 'gn', 'gu', 'ha', 'haw', 'hi', 'hr', 'ht', 'hu',
		'hy', 'ia', 'id', 'ig', 'is', 'it', 'iw', 'ja', 'jw', 'ka', 'kg', 'kk',
		'km', 'kn', 'ko', 'kri', 'ku', 'ky', 'la', 'lg', 'ln', 'lo', 'loz', 'lt',
		'lua', 'lv', 'mfe', 'mg', 'mi', 'mk', 'ml', 'mn', 'mo', 'mr', 'ms', 'mt',
		'ne', 'nl', 'nn', 'no', 'nso', 'ny', 'nyn', 'oc', 'om', 'or', 'pa', 'pcm',
		'pl', 'ps', 'pt-BR', 'pt-PT', 'qu', 'rm', 'rn', 'ro', 'ru', 'rw', 'sd',
		'sh', 'si', 'sk', 'sl', 'sn', 'so', 'sq', 'sr', 'sr-ME', 'st', 'su', 'sv',
		'sw', 'ta', 'te', 'tg', 'th', 'ti', 'tk', 'tl', 'tn', 'to', 'tr', 'tt',
		'tum', 'tw', 'ug', 'uk', 'ur', 'uz', 'vi', 'wo', 'xh', 'xx-bork',
		'xx-elmer', 'xx-hacker', 'xx-klingon', 'xx-pirate', 'yi', 'yo', 'zh-CN',
		'zh-TW', 'zu'
		)

	def search(self, items):

		def search_item(item, retry=0):
			url_search = f"https://www.google.{random.choice(self.domains)}/search?q={item.replace(' ', '+')}&num={self.results}&hl={random.choice(self.languages)}"
			__urls = []
			try:
				response = requests.get(url_search, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})
			except Exception:
				while retry < self.retry and not __urls:
					__urls = search_item(item=item, retry=retry + 1)
				return __urls
			else:
				soup = BeautifulSoup(response.text, 'html.parser')
				result_block = soup.find_all('div', attrs={'class': 'g'})
				for result in result_block:
					link = result.find('a', href=True)
					title = result.find('h3')
					if link and title:
						if str(link['href']).startswith("http"):
							__urls.append(link['href'])
				return __urls
			finally:
				logger.debug(f"SEARCHED URL → {url_search} RETRIES → {retry}")

		assert len(items) > 0
		logger.debug(f"ITEMS 4 SEARCH → {items}")
		self.makedirs(items=items)
		for item in items:
			__lnks = search_item(item=str(item))
			if __lnks:
				self.search_results.append({"item": item, "links": __lnks})
				time.sleep(random.uniform(self.sleep_min, self.sleep_max))
				if self.cache:
					self.cache_json()
			else:
				continue
		if self.search_results:
			if self.show_results:
				self.show()
			if self.pdf_report:
				self.pdf_reports()
			if self.use_social_search:
				self.use_social()


class Searx(Search):

	domains = (
		'7m.ee', 'bar', 'bissisoft.com', 'decatec.de', 'devol.it',
		'divided-by-zero.eu', 'dresden.network', 'feneas.org', 'fmac.xyz',
		'gnu.style', 'lelux.fi', 'likkle.monster', 'lnode.net', 'mastodontech.de',
		'mdosch.de', 'monicz.pl', 'mxchange.org', 'nakhan.net', 'nevrlands.de',
		'ninja', 'nixnet.services', 'openhoofd.nl', 'org', 'prvcy.eu', 'pwoss.org',
		'rasp.fr', 'roflcopter.fr', 'roughs.ru', 'ru', 'silkky.cloud', 'sk',
		'sp-codes.de', 'sunless.cloud', 'tux.land', 'tyil.nl', 'webheberg.info',
		'xyz', 'zackptg5.com'
		)

	languages = (
		'af-ZA', 'all', 'ar-EG', 'be-BY', 'bg-BG', 'ca-ES', 'cs-CZ', 'da-DK',
		'de', 'de-AT', 'de-CH', 'de-DE', 'el-GR', 'en', 'en-AU', 'en-CA', 'en-GB',
		'en-IE', 'en-IN', 'en-NZ', 'en-PH', 'en-SG', 'en-US', 'es', 'es-AR',
		'es-CL', 'es-ES', 'es-MX', 'et-EE', 'fa-IR', 'fi-FI', 'fr', 'fr-BE',
		'fr-CA', 'fr-CH', 'fr-FR', 'he-IL', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID',
		'is-IS', 'it-IT', 'ja-JP', 'ko-KR', 'lt-LT', 'lv-LV', 'ms-MY', 'nb-NO',
		'nl', 'nl-BE', 'nl-NL', 'pl-PL', 'pt', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU',
		'sk-SK', 'sl-SI', 'sr-RS', 'sv-SE', 'sw-TZ', 'th-TH', 'tr-TR', 'uk-UA',
		'vi-VN', 'zh', 'zh-CN', 'zh-TW'
		)

	def search(self, items):

		def search_item(item, retry=0):
			url_search = f"http://searx.{random.choice(self.domains)}/search?q={item.replace(' ', '+')}&format=json&language={random.choice(self.languages)}"
			__urls = []
			try:
				response = requests.get(url_search, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})
				if response.status_code == 429:
					raise Exception
				r_json = response.json()
				if len(r_json["results"]) <= 0:
					raise Exception
			except Exception:
				while retry < self.retry and not __urls:
					__urls = search_item(item=item, retry=retry + 1)
				return __urls
			else:
				__urls = [r["url"] for r in r_json["results"] if "url" in r]
				return __urls
			finally:
				logger.debug(f"SEARCHED URL → {url_search} RETRIES → {retry}")

		assert len(items) > 0
		logger.debug(f"ITEMS 4 SEARCH → {items}")
		self.makedirs(items=items)
		for item in items:
			__lnks = search_item(item=str(item))[:self.results]
			if __lnks:
				self.search_results.append({"item": item, "links": __lnks})
				time.sleep(random.uniform(self.sleep_min, self.sleep_max))
				if self.cache:
					self.cache_json()
			else:
				continue
		if self.search_results:
			if self.show_results:
				self.show()
			if self.pdf_report:
				self.pdf_reports()
			if self.use_social_search:
				self.use_social()


class Rambler(Search):

	def search(self, items):

		def search_item(item, retry=0):
			url_search = f"https://nova.rambler.ru/search?query={quote(item.replace(' ', '+'))}&utm_source=search_r0&utm_campaign=self_promo&utm_medium=form&utm_content=search"
			__urls = []
			try:
				response = requests.get(url_search)
			except Exception:
				while retry < self.retry and not __urls:
					__urls = search_item(item=item, retry=retry + 1)
				return __urls
			else:
				soup = BeautifulSoup(response.text, 'html.parser')
				results = soup.find_all('article')
				for result in results:
					link = result.find_all('a')[0]['href']
					if "yabs.yandex.ru" in link:
						continue
					else:
						if str(link).startswith("http"):
							__urls.append(link)
				return __urls
			finally:
				logger.debug(f"SEARCHED URL → {url_search} RETRIES → {retry}")

		assert len(items) > 0
		logger.debug(f"ITEMS 4 SEARCH → {items}")
		self.makedirs(items=items)
		for item in items:
			__lnks = search_item(item=str(item))
			if __lnks:
				self.search_results.append({"item": item, "links": __lnks})
				time.sleep(random.uniform(self.sleep_min, self.sleep_max))
				if self.cache:
					self.cache_json()
			else:
				continue
		if self.search_results:
			if self.show_results:
				self.show()
			if self.pdf_report:
				self.pdf_reports()
			if self.use_social_search:
				self.use_social()


class Social(metaclass=abc.ABCMeta):
	def __init__(
		self, posts_limit=10,
		export_data=True,
		export_format="csv",
		download_media=True
		):
		self.posts_limit = posts_limit
		self.export_data = export_data
		self.export_format = export_format
		self.download_media = download_media
		self.export_formats = ['csv', 'xls', 'html', 'json']
		self.stop_words = ["explore", "tags", "wall", "music"]

	@abc.abstractmethod
	def search(self):
		pass

	def export(self, social_net, array, username):
		data = pd.DataFrame(array)
		if self.export_format in self.export_formats[:3]:
			f = {
				self.export_formats[0]: data.to_csv,
				self.export_formats[1]: data.to_excel,
				self.export_formats[2]: data.to_html
				}
			f[self.export_format](f'{os.path.join(__base__, username, social_net)}.{self.export_format}', index=False)
		if self.export_format == self.export_formats[3]:
			with open(f'{os.path.join(__base__, username, social_net)}.{self.export_format}', "w") as f:
				json.dump({social_net: array}, f)
		logger.debug(f'{social_net} → {os.path.join(__base__, username, social_net)}.{self.export_format}')

	def get_user_from_link(self, link):
		return link.split('/')[3] if not (
			link.split('/')[3] in self.stop_words
			) else None


class Instagram(Social):

	def search(self, link, searched_item):
		logger.debug(f"{s_ig} {link}")
		user = self.get_user_from_link(link)
		if self.download_media and not(user is None):
			os.chdir(os.path.join(__base__, searched_item, s_ig))
			'''ig = Instaloader()
			profile = Profile.from_username(ig.context, user)
			posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda p: p.likes + p.comments, reverse=True)
			for post in islice(posts_sorted_by_likes, ceil(self.posts_limit)):
				ig.download_post(post, user)'''
			try:
				os.system(f"instaloader {user} --count {self.posts_limit}")
			except Exception as e:
				logger.debug(f"{s_ig} {user} {str(e)}")
			os.chdir(__base__)
		return user


class Vk(Social):
	def search(self, link, searched_item):

		def __search(user):
			for l, vk in enumerate(sns_vk.VKontakteUserScraper(user).get_items()):
				if l == self.posts_limit:
					break
				yield {'url': vk.url, 'content': vk.content}

		logger.debug(f"{s_vk} → {link}")
		user = self.get_user_from_link(link)
		if user is None:
			return user
		else:
			if self.export_data:
				self.export(
					social_net=s_vk,
					array=__search(user=user),
					username=searched_item
					)
			return __search(user=user)


class Telegram(Social):
	def search(self, link, searched_item):

		def __search(user):
			for l, tg in enumerate(sns_tg.TelegramChannelScraper(name=user).get_items()):
				if l == self.posts_limit:
					break
				yield {'date': tg.date, 'url': tg.url, 'content': tg.content}

		logger.debug(f"{s_tg} → {link}")
		user = self.get_user_from_link(link)
		if user is None:
			return user
		else:
			if self.export_data:
				self.export(
					social_net=s_tg,
					array=__search(user=user),
					username=searched_item
					)
			return __search(user=user)


class Facebook(Social):
	def search(self, link, searched_item):

		def __search(user):
			for l, fb in enumerate(get_posts(user, pages=self.posts_limit)):
				if l == self.posts_limit:
					break
				yield fb

		logger.debug(f"{s_fb} → {link}")
		user = self.get_user_from_link(link)
		if user is None:
			return user
		else:
			if self.export_data:
				self.export(
					social_net=s_fb,
					array=__search(user=user),
					username=searched_item
					)
			return __search(user=user)


class Twitter(Social):
	def search(self, link, searched_item):

		def __search(user):
			for l, tw in enumerate(sns_tw.TwitterSearchScraper(query=user).get_items()):
				if l == self.posts_limit:
					break
				yield {'username': tw.username, 'url': tw.url, 'content': tw.content}

		logger.debug(f"{s_tw} → {link}")
		user = self.get_user_from_link(link)
		if user is None:
			return user
		else:
			if self.export_data:
				self.export(
					social_net=s_tw,
					array=__search(user=user),
					username=searched_item
					)
			return __search(user=user)


class Youtube(Social):

	@staticmethod
	def get_user_from_link(link):
		return link.split('/')[4] if (
			(link.split('/')[3] == "channel") or
			(link.split('/')[3] == "c")
			) else None

	def search(self, link, searched_item):
		logger.debug(f"{s_yt} → {link}")
		user = self.get_user_from_link(link)
		if self.download_media:
			os.chdir(os.path.join(__base__, searched_item, s_yt))
			try:
				os.system(f"youtube-dl {link} --playlist-end {self.posts_limit}")
			except Exception as e:
				logger.debug(f"{s_yt} {link} {str(e)}")
			os.chdir(__base__)
		return user


class Tumblr(Social):

	@staticmethod
	def get_user_from_link(link):
		return link.split("/")[2].split(".")[0]

	def search(self, link, searched_item):

		def __search(client, user):
			for x in client.posts(user)['posts']:
				if x["type"] == "photo":
					for ph in x["photos"]:
						yield ("media", ph["original_size"]["url"])
				if x["type"] == "video":
					if x["video_type"] == s_tb:
						yield ("media", x["video_url"])
					if x["video_type"] == s_yt:
						yield ("youtube", x['permalink_url'])

		logger.debug(f"{s_tb} → {link}")
		user = self.get_user_from_link(link)
		if self.download_media:
			os.chdir(os.path.join(__base__, searched_item, s_tb))
			client = Tumblpy(
				app_key='zLgPh6LeV7DyczfPALkTEfr8rOgzcYAY8TzAlabVIYrgpATPON',
				app_secret='mGP5mVle2ZUNKHzK4ayjAGpfUCkLTmQm91ic9YtWTTcDkdFLPE',
				oauth_token='hRwAn1CoZJ5Q96T8o51aQL2YcKnh1k66RlnCRLQtqjtWf0WZ4W',
				oauth_token_secret='oqlple5FP9MVRTxbUQHjrEVSs4DDLFP7h4zBE5D4g952qeqRo3')
			try:
				youtube = Youtube(
					posts_limit=self.posts_limit,
					export_data=self.export_data,
					export_format=self.export_format,
					download_media=self.download_media
					)
				for __type, __url in __search(client=client, user=user):
					if __type == "media":
						with open(__url.split("/")[-1], "wb") as f:
							f.write(requests.get(__url, allow_redirects=True).content)
					if __type == "youtube":
						youtube.search(link=__url, searched_item=searched_item["item"])
			except Exception as e:
				logger.debug(f"{s_tb} {link} {str(e)}")
			os.chdir(__base__)
		return user


class Tiktok(Social):

	@staticmethod
	def get_user_from_link(link):
		if "?" in link.split("/")[3]:
			return link.split("/")[3][1:link.split("/")[3].index("?")] if link.split("/")[3].startswith("@") else None
		else:
			return link.split("/")[3][1:] if link.split("/")[3].startswith("@") else None

	def search(self, link, searched_item):
		logger.debug(f"{s_tk} → {link}")
		user = self.get_user_from_link(link)
		if user is None:
			return user
		else:
			tks = []
			try:
				tik_tok.run(user)
				tks.append({
					"nickname": tik_tok.nickname(),
					"followers": tik_tok.followers(),
					"following": tik_tok.following(),
					"likes": tik_tok.likes(),
					"status": tik_tok.status(),
					"avatar_link": tik_tok.getavatar()
					})
			except Exception as e:
				logger.debug(f"{s_tk} {link} {str(e)}")
			else:
				if self.export_data:
					self.export(social_net=s_tk, array=tks, username=searched_item)
			return tks


class Snapchat(Social):

	@staticmethod
	def get_user_from_link(link):
		return link.split("/")[4] if (
			(link.split('/')[3] == "u") or 
			(link.split('/')[3] == "add")
			) else None

	def search(self, link, searched_item):
		logger.debug(f"{s_sc} → {link}")
		user = self.get_user_from_link(link)
		if self.download_media and not(user is None):
			os.chdir(os.path.join(__base__, searched_item, s_sc))
			try:
				os.system(f"snapchat-dl {user} -l {self.posts_limit}")
			except Exception as e:
				logger.debug(f"{s_sc} {link} {str(e)}")
			os.chdir(__base__)
		return user


class PDF:

	def __init__(self, path, summary_params):
		self.__path = path
		self.__summary_types = ("words", "ratio")
		self.__summary_type, self.__summary_value = summary_params
		self.__text = textract.process(self.__path)
		self.__text_decoded = self.__text.decode(
			chardet.detect(self.__text)['encoding'])
		self.__langs = {
			"ar": "arabic",
			"da": "danish",
			"nl": "dutch",
			"en": "english",
			"fi": "finnish",
			"fr": "french",
			"de": "german",
			"hu": "hungarian",
			"it": "italian",
			"nb": "norwegian",
			"pl": "polish",
			"pt": "portuguese",
			"ro": "romanian",
			"ru": "russian",
			"es": "spanish",
			"sv": "swedish"
			}

	@property
	def text(self):
		return self.__text

	@property
	def summary(self):
		try:
			__lang = langdetect.detect(self.__text_decoded)
		except langdetect.lang_detect_exception.LangDetectException as e:
			self.__summary = str(e)
		else:
			if __lang in self.__langs:
				if self.__summary_type in self.__summary_types:
					if self.__summary_type is self.__summary_types[0]:
						self.__words = len(self.__text_decoded.split())
						if self.__summary_value > self.__words:
							self.__summary_value = self.__words
						self.__summary = summarizer.summarize(
							self.__text_decoded,
							language=self.__langs[__lang],
							words=self.__summary_value)
					if self.__summary_type is self.__summary_types[1]:
						if 0 < self.__summary_value < 1:
							self.__summary = summarizer.summarize(
								self.__text_decoded,
								language=self.__langs[__lang],
								ratio=self.__summary_value)
						else:
							self.__summary = f"VALUE MUST BE IN RANGE (0,1) NOT: {self.__summary_value}"
				else:
					self.__summary = f"CHOOSE ONE OF TYPE SUMMARIZING: {self.__summary_types}"
			else:
				self.__summary = f"CAN'T SUMMARIZE TEXT FOR LANG: {__lang}"
		return self.__summary

	@property
	def keywords(self):
		try:
			__kw = iter((keywords.keywords(self.__text_decoded)).splitlines())
		except MemoryError:
			self.__keywords = "MemoryError"
		else:
			self.__keywords = iter(__kw)
		return self.__keywords

	@property
	def urls(self):

		def __url():
			document = PyPDF2.PdfFileReader(self.__path)
			for page in range(document.numPages):
				pdf_page = document.getPage(page)
				if '/Annots' in pdf_page:
					for item in (pdf_page['/Annots']):
						pdf_obj = item.getObject()
						if "/A" in pdf_obj:
							if "/URI" in pdf_obj["/A"]:
								yield pdf_obj["/A"]["/URI"]
		self.__urls = __url()  # set()
		return self.__urls


__all__ = ["Google", "Rambler", "Searx"]
