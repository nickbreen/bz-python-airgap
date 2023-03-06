from yarl import URL

if __name__ == "__main__":
    url = URL('https://www.python.org/~guido?arg=1#frag')
    print("URL: %s" % url)