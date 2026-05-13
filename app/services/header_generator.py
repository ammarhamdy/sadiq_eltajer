import random


def default_headers():
    return {
        "Host": "sadiq-eltajer.sa",
        "User-Agent": (
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:150.0) "
            "Gecko/20100101 Firefox/150.0"
        ),
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://sadiq-eltajer.sa/",
        "X-App-Api-Token": "o3fNzP7ZeAX97q5mjjtqRVon51jrOol8",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=4",
        "Te": "trailers",
    }

def random_headers():
    firefox_versions = [120, 121, 122, 123, 124, 125, 126, 127]
    os_options = [
        "X11; Linux x86_64",
        "X11; Ubuntu; Linux x86_64",
        "Windows NT 10.0; Win64; x64",
    ]

    languages = [
        "en-US,en;q=0.9",
        "en-GB,en;q=0.8",
        "en-US,en;q=0.7,ar;q=0.3",
    ]

    accepts = [
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "text/html,application/xml;q=0.9,*/*;q=0.8",
    ]

    encodings = [
        "gzip, deflate, br",
        "gzip, deflate",
    ]

    firefox_version = random.choice(firefox_versions)
    os_part = random.choice(os_options)

    headers = {
        "User-Agent": f"Mozilla/5.0 ({os_part}; rv:{firefox_version}.0) Gecko/20100101 Firefox/{firefox_version}.0",
        "Accept": random.choice(accepts),
        "Accept-Language": random.choice(languages),
        # "Accept-Encoding": random.choice(encodings),
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.ber.org.sa",
        "Referer": "https://www.ber.org.sa/rafed/",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": str(random.choice([0, 1]))
    }

    return headers
