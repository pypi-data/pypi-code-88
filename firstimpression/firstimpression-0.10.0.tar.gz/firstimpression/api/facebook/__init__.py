def get_page_name(post):
    return post['page_name']


def get_thumbnail_url(post):
    return post['thumbnail']


def get_likes(post):
    return post['likes']


def get_message(post):
    return post['message']


def get_created_at(post):
    return post['created_at']


def crop_message(text, max_length):
    if len(text) > max_length:
        return text[:max_length-3] + "...\nLees verder op Facebook"
    else:
        return text
