import asyncio
import json
import datetime
import threading
import time

from progress.bar import Bar
import requests
from selenium import webdriver
from selenium.common.exceptions import JavascriptException, NoSuchElementException
from selenium.webdriver import ActionChains
import chromedriver_binary
import websockets


TIMEOUT=300
ENVIRONMENTS = {
    'local': 'LOCAL',
    'cloud': 'DC',
    'unblockable': 'RESID',
}
SCROLL_SPEEDS = {
    'fast': 'FAST',
    'medium': 'MEDIUM',
    'slow': 'SLOW',
}
FORMATS = {
    'json': 'json_format',
    'csv': 'csv_format',
}
OUTPUTS = set(['data', 'file'])
STARTING_LIMIT = 64
MAX_RESPONSE_THRESHOLD = 2 ** 20


class ScraperRunError(Exception):
    def __init__(self, message, last_url):
        super().__init__(message)
        self.last_url = last_url


class Client:
    def __init__(self, username, password, host='parsagon.io'):
        data = {'username': username, 'password': password}
        r = requests.post(f'https://{host}/api/accounts/token-auth/', json=data, timeout=TIMEOUT)
        if not r.ok:
            self._display_errors(r)
        self.token = r.json()['token']
        self.host = host

    def _display_errors(self, response):
        if response.status_code == 500:
            raise Exception('A server error occurred. Please notify Parsagon.')
        if response.status_code in (502, 503, 504):
            raise Exception('Lost connection to server. To try again later, rerun execute() with retry=True')
        errors = response.json()
        if 'non_field_errors' in errors:
            raise Exception(errors['non_field_errors'])
        else:
            raise Exception(errors)

    async def _scroll(self, driver, speed):
        if speed == 'FAST':
            driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
            await asyncio.sleep(1)
        elif speed == 'MEDIUM':
            position = driver.execute_script("return window.pageYOffset;")
            page_height = driver.execute_script("return document.body.scrollHeight;")
            for i in range(1, 6):
                new_position = position + (page_height - position) * i / 5
                driver.execute_script(f"window.scrollTo({{top: {new_position}, behavior: 'smooth'}});")
                await asyncio.sleep(0.5)
                new_elems = driver.execute_script("return document.querySelectorAll(':not([data-parsagon-io-marked])').length;")
                if new_elems:
                    break
            await asyncio.sleep(0.5)
        elif speed == 'SLOW':
            position = driver.execute_script("return window.pageYOffset;")
            page_height = driver.execute_script("return document.body.scrollHeight;")
            for i in range(1, 11):
                new_position = position + (page_height - position) * i / 10
                driver.execute_script(f"window.scrollTo({{top: {new_position}, behavior: 'smooth'}});")
                await asyncio.sleep(1)
                new_elems = driver.execute_script("return document.querySelectorAll(':not([data-parsagon-io-marked])').length;")
                if new_elems:
                    break
            await asyncio.sleep(1)

    async def _handle_driver(self, result_id, exit_event):
        driver = webdriver.Chrome()
        async with websockets.connect(f'wss://{self.host}/ws/scrapers/results/{result_id}/client/') as websocket:
            while not exit_event.is_set():
                try:
                    message_str = await asyncio.wait_for(websocket.recv(), timeout=2)
                except asyncio.TimeoutError:
                    continue
                message = json.loads(message_str)
                convo_id = message['convo_id']
                response = 'OK'
                command = message['command']
                if command == 'get':
                    driver.get(message['url'])
                    await asyncio.sleep(2)
                elif command == 'mark':
                    elem_idx = driver.execute_script(f"let elemIdx = {message['elem_idx']}; for (const node of document.querySelectorAll(':not([data-parsagon-io-marked])')) {{ node.setAttribute('data-parsagon-io-marked', elemIdx); elemIdx++; }} return elemIdx;")
                    await websocket.send(json.dumps({'response': elem_idx, 'convo_id': convo_id}))
                    continue
                elif command == 'scroll':
                    await self._scroll(driver, message['speed'])
                elif command == 'click':
                    actions = ActionChains(driver)
                    target = driver.find_element_by_xpath(f"//*[@data-parsagon-io-marked={message['target_id']}]")
                    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", target)
                    await asyncio.sleep(0.5)
                    try:
                        actions.move_to_element(target).click().perform()
                        await asyncio.sleep(2)
                        await self._scroll(driver, message['speed'])
                    except JavascriptException:
                        pass
                elif command == 'inspect':
                    query = message['query']
                    if query == 'url':
                        response = driver.current_url
                    elif query == 'page_source':
                        response = driver.page_source
                    elif query == 'target_data':
                        try:
                            target = driver.find_element_by_xpath(f"//*[@data-parsagon-io-marked={message['target_id']}]")
                            tag = target.tag_name
                            text = target.text
                            href = target.get_attribute('href')
                            url = driver.execute_script(f"return document.querySelector('[data-parsagon-io-marked=\"{message['target_id']}\"]').href;")
                            response = {'tag': tag, 'text': text, 'href': href, 'url': url}
                        except NoSuchElementException:
                            response = {'tag': None}
                await websocket.send(json.dumps({'response': response, 'convo_id': convo_id}))
        driver.quit()

    def _run_driver(self, result_id, exit_event):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._handle_driver(result_id, exit_event))
        loop.close()

    def _get_result(self, result_id, format, output, file_path, urls):
        headers = {'Content-Type': 'application/json', 'Authorization': f'Token {self.token}'}
        r = requests.post(f'https://{self.host}/api/scrapers/results/{result_id}/execute/', headers=headers, timeout=TIMEOUT)
        if not r.ok:
            self._display_errors(r)
        bar = Bar('Collecting data', max=len(urls), suffix='%(percent)d%%')
        num_scraped = 0
        while True:
            r = requests.get(f'https://{self.host}/api/scrapers/results/{result_id}/progress/', headers=headers, timeout=TIMEOUT)
            if not r.ok:
                self._display_errors(r)
            result_data = r.json()
            if result_data['status'] == 'FINISHED':
                for i in range(len(urls) - num_scraped):
                    bar.next()
                bar.finish()
                break
            elif result_data['status'] == 'ERROR':
                bar.finish()
                raise ScraperRunError('A server error occurred. Please notify Parsagon.', result_data['current_url'])
            elif 'num_scraped' in result_data and result_data['num_scraped'] > num_scraped:
                for i in range(result_data['num_scraped'] - num_scraped):
                    bar.next()
                num_scraped = result_data['num_scraped']

            time.sleep(5)

        print('Downloading data...')
        if output == 'file':
            with open(file_path, 'w') as f:
                if format == 'csv':
                    raise Exception("Output type 'file' not yet supported for format 'csv'")
                else:
                    offset = 0
                    limit = STARTING_LIMIT
                    offset_incr = 0
                    max_response_size = 0
                    r = requests.get(f'https://{self.host}/api/scrapers/results/{result_id}/download/?data_format={format}&offset={offset}&limit={limit}', headers=headers, timeout=TIMEOUT)
                    if not r.ok:
                        self._display_errors(r)
                    result_data = r.json()
                    offset_incr = len(result_data['result'])
                    offset += offset_incr
                    new_data = json.dumps(result_data)
                    f.write(new_data[:-2])
                    max_response_size = max(max_response_size, len(new_data))

                    while offset_incr == limit:
                        if max_response_size < MAX_RESPONSE_THRESHOLD:
                            limit *= 2

                        r = requests.get(f'https://{self.host}/api/scrapers/results/{result_id}/download/?data_format={format}&offset={offset}&limit={limit}', headers=headers, timeout=TIMEOUT)
                        if r.status_code == 504:
                            if limit == 1:
                                raise Exception('Data download timed out')
                            limit //= 2
                            offset_incr = limit
                            max_response_size = MAX_RESPONSE_THRESHOLD
                            continue
                        if not r.ok:
                            self._display_errors(r)
                        result_data = r.json()
                        offset_incr = len(result_data['result'])
                        if not offset_incr:
                            break
                        offset += offset_incr
                        new_data = json.dumps(result_data['result'])
                        new_data = ',' + new_data[1: -1]
                        f.write(new_data)
                        max_response_size = max(max_response_size, len(new_data))
                    f.write('}}')
        else:
            r = requests.get(f'https://{self.host}/api/scrapers/results/{result_id}/download/?data_format={format}',
                             headers=headers, timeout=TIMEOUT)
            if not r.ok:
                self._display_errors(r)
            data = r.json()
            if format == 'csv':
                return data['result']
            else:
                return data

    def execute(self, scraper_name, urls, env, max_page_loads=1, scroll_speed='fast', action_settings={}, format='json', output='data', file_path='', is_retry=False):
        if env not in ENVIRONMENTS:
            raise ValueError("Environment must be 'local', 'cloud', or 'unblockable'")
        if scroll_speed not in SCROLL_SPEEDS:
            raise ValueError("Scroll speed must be 'fast', 'medium', or 'slow'")
        if format not in FORMATS:
            raise ValueError("Format must be 'json' or 'csv'")
        if output not in OUTPUTS:
            raise ValueError("Output must be 'data' or 'file'")
        if output == 'file' and not file_path:
            raise ValueError("Output type is 'file' but no file path was given")

        headers = {'Content-Type': 'application/json', 'Authorization': f'Token {self.token}'}

        data = {'scraper_name': scraper_name, 'urls': urls, 'max_page_loads': max_page_loads, 'scroll_speed': SCROLL_SPEEDS[scroll_speed], 'action_settings': action_settings, 'environment': ENVIRONMENTS[env], 'is_retry': is_retry}
        r = requests.post(f'https://{self.host}/api/scrapers/results/find-redundant/', headers=headers, json=data, timeout=TIMEOUT)
        if not r.ok:
            self._display_errors(r)
        result = r.json()

        if not result.get('id2'):
            data = {'scraper_name': scraper_name, 'urls': urls, 'max_page_loads': max_page_loads, 'scroll_speed': SCROLL_SPEEDS[scroll_speed], 'action_settings': action_settings}
            r = requests.post(f'https://{self.host}/api/scrapers/runs/', headers=headers, json=data, timeout=TIMEOUT)
            if not r.ok:
                self._display_errors(r)
            run = r.json()

            if not run['scraper'][FORMATS[format]]:
                raise Exception(f'{format} format is unavailable for this scraper')

            data = {'environment': ENVIRONMENTS[env]}
            r = requests.post(f'https://{self.host}/api/scrapers/runs/{run["id2"]}/results/', headers=headers, json=data, timeout=TIMEOUT)
            if not r.ok:
                self._display_errors(r)
            result = r.json()
        elif not result['scraper'][FORMATS[format]]:
            raise Exception(f'{format} format is unavailable for this scraper')

        if env == 'local':
            exit_event = threading.Event()
            driver_task = threading.Thread(target=self._run_driver, args=[result['id2'], exit_event])
            driver_task.start()
            time.sleep(5)

        current_url = result['current_url']
        while True:
            try:
                return_value = self._get_result(result['id2'], format, output, file_path, urls)
                break
            except ScraperRunError as e:
                if current_url == e.last_url:
                    if env == 'local':
                        exit_event.set()
                        time.sleep(2.1)
                    raise e
                else:
                    current_url = e.last_url

        if env == 'local':
            exit_event.set()
            time.sleep(2.1)

        return return_value
