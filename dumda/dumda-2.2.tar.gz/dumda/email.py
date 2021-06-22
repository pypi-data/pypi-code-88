from random import choice


def generate_email(fullname: str):
    """
    returns a string of a generated email
    for a user based on a passed full name
    :param fullname: 
    :return: 
    """
    user_format = choice(['fi last', 'first li', 'first last'])
    if user_format == 'fi last':
        user = (fullname.split()[0][0] + fullname.split()[1]).lower()
    elif user_format == 'first li':
        user = (fullname.split()[0] + fullname.split()[1][0]).lower()
    else:
        user = (fullname.split()[0] + fullname.split()[1]).lower()
        
    domains = ['foo', 'bar', 'baz', 'qux']
    extensions = ['.com', '.net', '.org']
    
    domain = "@" + choice(domains) + choice(extensions)
    
    email = user + domain
    return email
