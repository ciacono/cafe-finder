import populartimes
import datetime
from os import environ

cur_hour = datetime.datetime.now().hour
weekdate = datetime.datetime.today().weekday()


class Cafe:
    def __init__(self, name, address, rating, score):
        self.name = name
        self.address = address
        self.rating = rating
        self.score = score


c1 = Cafe("Arizona Biltmore Golf Club", "2818 E Camino Acequia Drive", 4.0, 80)
c2 = Cafe("JJ Bean", "10000 Water Rd.", 0.1, 40)
c3 = Cafe("Bean Around the World", "3 UBC Blvd.", 2.0, 99)
c4 = Cafe("Greenhorn", "494848 Pender St.", 3.1, 10)
c5 = Cafe("Water St. Cafe", "9999 Denman St.", 5.0, 70)


# Returns a list of dictionaries, containing cafes 1km around lat, long
def get_locations(lat, lon):
    dist = 0.0089
    min_lat = lat - dist
    max_lat = lat + dist
    min_lon = lon - dist
    max_lon = lon + dist
    return populartimes.get(environ["APIKEY"], ["cafe"], (min_lat, min_lon), (max_lat, max_lon), 20, 1000)


def sorting(item):
    if item.get("current_popularity") is not None and item["current_popularity"] != 0:
        return item["current_popularity"]
    return item["populartimes"][weekdate]["data"][cur_hour]


def good_locations(lat, lon):
    good_loc = []
    for location in get_locations(lat, lon):
        if location.get("current_popularity") is not None:
            good_loc.append(location)
            continue
        if location["populartimes"][weekdate]["data"][cur_hour] != 0:
            good_loc.append(location)

    return sorted(good_loc, key=sorting)
