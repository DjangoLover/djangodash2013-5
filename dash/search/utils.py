import re
from string import split

from users.models import User
from music.models import MusicProfile
def parse_search(search_string):

    # remove all non-alpha chars
    cleaned_string = re.sub(r'\W+', ' ', search_string)

    # split search string on whitespace
    terms = split(cleaned_string)

    return terms


def do_find(user, search_query):

    ZIPCODE = re.compile('\d{5}')

    #terms = parse_search(search_query)

    # get zipcodes
    zipcodes = re.findall(ZIPCODE, search_query)

    # make a list of users, minus admins
    profiles = MusicProfile.objects.all()
    profile_list = [p for p in profiles if p.user.is_staff == False]

    # first find matching users on zipcodes
    zip_matches = []
    for p in profile_list:
        if p.zipcode in zipcodes:
            if not p.user == user:
                zip_matches.append(p.user)

    # combine results
    user_matches = zip_matches

    return user_matches
