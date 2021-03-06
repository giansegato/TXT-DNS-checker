import subprocess
import os
import time
import sys

if len(sys.argv) > 1:
    _DOMAIN = sys.argv[1]
    if len(sys.argv) > 2:
        _TARGET = sys.argv[2]
    else:
        _TARGET = 'google-site-verification'
else:
    _DOMAIN = 'giansegato.com'
_SECONDS = 30

def notify(title, text):
    # MacOS X only compatible
    os.system("""
        osascript -e 'display notification "{}" with title "{}"'
    """.format(text, title))

def target_in_dns(domain, target):
    # Linux and MacOS X compatible
    result = subprocess.run(['dig', domain, 'any'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return target in result

if __name__ == "__main__":

    print("Checking", end='')
    while not target_in_dns(_DOMAIN, _TARGET):
        print('.', end='', flush=True)
        time.sleep(_SECONDS)

    notify("DNS Record", "{} verified!".format(_DOMAIN))