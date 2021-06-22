def crop_message(text, max_length, language):
    if language == 1:
        append_text = "Lees verder op Instagram"
    else:
        append_text = "Read more on Instagram"

    if len(text) > max_length:
        return text[:max_length-3] + "...\n{}".format(append_text)
    else:
        return text


def get_subscription_name(post):
    return post['subscribed_to']


def get_thumbnail_url(post):
    return post['thumbnail_url']


def get_message(post):
    return post['message']


def get_creation_date(post):
    return post['created_at']


def get_hashtags(post):
    hashtags = post['hashtags']
    return ' '.join(hashtags)
