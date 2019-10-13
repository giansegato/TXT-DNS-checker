# TXT DNS Checker

This script runs in the background and every `_SECONDS` seconds checks the TXT DNS record of the `_DOMAIN` web domain. As soon as it finds a target string (`_TARGET`), it notifies the user with a system notification.

## Why?

It's been developed when deploying a website to the Firebase hosting, where in case of custom domain you have to verify the ownership of the website by editing the TXT DNS record of the domain, but the use cases can be several others.

## How?

Edit the `_DOMAIN` and `_TARGET` variables to your needs. Then run the script (`python3 check.py`).
No external script dependency. Working only with Python 3.x onwards.

## Room for improvement

The system function the notifies the user is currently working only on MacOS. The DNS lookup call is working only on UNIX-based systems.
