def like(link):
    import requests
    r = requests.get(link)
    t = r.text
    dlike = '"likeStatus":"INDIFFERENT","tooltip":'
    gr = t.find(dlike)
    tt = t[gr+len(dlike):]
    y = tt.find("}")
    rez = t[gr+len(dlike):gr+len(dlike)+y]
    sla = rez.find("/")
    return rez[1:sla-1]

def dislike(link):
    import requests
    r = requests.get(link)
    t = r.text
    dlike = '"likeStatus":"INDIFFERENT","tooltip":'
    gr = t.find(dlike)
    tt = t[gr+len(dlike):]
    y = tt.find("}")
    rez = t[gr+len(dlike):gr+len(dlike)+y]
    sla = rez.find("/")
    return rez[sla+2:-1]

def view(link):
    import requests
    r = requests.get(link)
    t = r.text
    fnd = 'itemprop="interactionCount" content='
    gg = t.find(fnd)
    ff = t[len(fnd)+1+gg:gg+99]
    nrt = ff.find("meta")
    return t[len(fnd)+1+gg:gg+nrt+len(fnd)-2]

def channel_name(link):
    import requests
    f = requests.get(link)
    t = f.text.find('<link itemprop="name" content="')
    fnd = '<link itemprop="name" content="'
    nxt = f.text[t+len(fnd):]
    gh = nxt.find(">")
    return f.text[t+len(fnd):t+len(fnd)+gh-1]

def title(link):
    import requests
    g = requests.get(link)
    fnd = '</title><meta name="title" content="'
    t = g.text.find(fnd)
    nxt = g.text[t+len(fnd):]
    tt = nxt.find(">")
    return g.text[t+len(fnd):t+len(fnd)+tt-1]

def channel_link(link):
    import requests
    gr = requests.get(link)
    t = gr.text
    fnd = '<link itemprop="url" href="http://www.youtube.com/channel/'
    h = t.find(fnd)
    nxt = t[h+len(fnd):]
    j = nxt.find(">")
    return t[h+len(fnd)-len("http://www.youtube.com/channel/"):h+len(fnd)+j-1]

def description(link):
    import requests
    gr = requests.get(link)
    t = gr.text
    fnd = ',"description":{"simpleText":"'
    h = t.find(fnd)
    nxt = t[h+len(fnd):]
    j = nxt.find("}")
    return t[h+len(fnd):h+len(fnd)+j-1].replace(r"\n", "\n")