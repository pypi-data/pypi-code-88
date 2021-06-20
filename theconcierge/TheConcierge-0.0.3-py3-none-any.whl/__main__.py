import os


theconcierge_template_url = "https://github.com/luigimalaguti/TheConciergeTemplate"
git_clone = "git clone {url}.git"


def main():
    os.system(git_clone.format(url=theconcierge_template_url))


if __name__ == "__main__":
    main()
