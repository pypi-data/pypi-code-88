import requests

def get_user_key(devkey, username, password):
    """This function retrives the user
    key of an account on pastebin."""
    url = 'https://pastebin.com/api/api_login.php'
    data = {'api_dev_key': devkey, 'api_user_name': username, 'api_user_password': password}
    r = requests.post(url, data=data)
    return r.text

def make_new_paste(devkey, paste_text, user_key=None,  paste_title=None, paste_format=None, paste_type=None, paste_expiry: int=None):
    """This function creates a new paste
    on pastebin with the given arguments."""
    data = {'api_dev_key': devkey, 'api_option': 'paste', 'api_paste_code': paste_text, 'api_paste_expire_date': f'{paste_expiry}M', 'api_paste_format': paste_format, 'api_user_key': user_key}
    r = requests.post('https://pastebin.com/api/api_post.php', data=data)
    return r.text

def list_pastes_user(devkey, userkey):
    """This function retrives a list
    of pastes created by a user on pastebin."""
    content = {'api_dev_key': devkey, 'api_user_key': userkey, 'api_results_limit': '100', 'api_option': 'list'}
    r = requests.post('https://pastebin.com/api/api_post.php', params=content)
    return r.text

def delete_paste(devkey, userkey, pastekey):
    """This function deletes the
    given paste of the given user
    on pastebin."""
    content = {'api_dev_key': devkey, 'api_user_key': userkey, 'api_paste_key': pastekey, 'api_option': 'delete'}
    r = requests.post('https://pastebin.com/api/api_post.php', params=content)
    return r.text
    
def user_settings_and_info(devkey, userkey):
    """This function retrives the user
    settings and information from pastebin."""
    content = {'api_dev_key': devkey, 'api_user_key': userkey,'api_option': 'userdetails'}
    r = requests.post('https://pastebin.com/api/api_post.php', params=content)
    return r.text

def get_raw_paste_content(devkey, userkey, pastekey):
    content = {'api_dev_key': devkey, 'api_user_key': userkey, 'api_paste_key': pastekey, 'api_option': 'show_paste'}
    r = requests.post('https://pastebin.com/api/api_post.php', params=content)
    return r.text