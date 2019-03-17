import populartimes
import datetime
from os import environ

cur_hour = datetime.datetime.now().hour
weekdate = datetime.datetime.today().weekday()


class Cafe:
    def __init__ (self, name, address, rating, score, ratings, busy, id):
        self.name = name
        self.address = address
        self.rating = rating
        self.score = score
        self.num_ratings = ratings
        self.busy = busy
        self.id = id
        self.link = "https://www.google.com/maps/place/?q=place_id:" + id


# Returns a list of dictionaries, containing cafes 1km around lat, long
def get_locations(lat, lon):
    dist = 0.0050
    min_lat = lat - dist
    max_lat = lat + dist
    min_lon = lon - dist
    max_lon = lon + dist
    return populartimes.get(environ["APIKEY"], ["cafe"], (min_lat, min_lon), (max_lat, max_lon), 20, 50)


def sort_cafes(locs, busy_pref, rating_pref):
    sorted_cafes = []
    scores = []
    for cafe in locs:
        if cafe.get("current_popularity") is not None and cafe["current_popularity"] != 0:
            popularity = cafe["current_popularity"]
        else:
            popularity = cafe["populartimes"][weekdate]["data"][cur_hour]

        score = int(round(((100 - popularity)*(busy_pref/100) + (1 - busy_pref/100)*cafe["rating"]*20)/2, 0))
        scores.append(score)
        if cafe["rating"] >= rating_pref:
            sorted_cafes.append(Cafe(cafe["name"], cafe["address"], cafe["rating"], int(score),
                                     cafe["rating"], popularity, cafe["id"]))
    sorted_cafes = sorted(sorted_cafes, key=lambda x: x.score, reverse=True)
    if scores:
        max_score = max(scores)
        for cafe in sorted_cafes:
            cafe.score = int(round((cafe.score / max_score)*100, 0))
    return sorted_cafes


def good_locations(lat, lon, busy_pref, rating_pref):
    good_loc = []
    for location in get_locations(lat, lon):
        if location.get("current_popularity") is not None:
            good_loc.append(location)
            continue
        if location["populartimes"][weekdate]["data"][cur_hour] != 0:
            good_loc.append(location)
    sorted_cafes = sort_cafes(good_loc, busy_pref, rating_pref)
    return sorted_cafes
