import sys
import requests
import hashlib
import os


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'Your password {password} was found {count} times, you should change your pass')
        else:
            print(f'Your pass {password} not found. You can use it.')
        return 'Done!'


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_chara, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first_5_chara)
    return get_password_leaks_count(response, tail)


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code}')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


if __name__ == 'main':
    sys.exit(main(sys.argv[1:]))
