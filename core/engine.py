import os
import pandas as pd
import math
# this below 2 lines was my default before live

df = pd.read_csv("core\places.csv")

places = df.to_dict(orient="records")

def haversine(lat1, lon1, lat2, lon2): 
    R = 6371
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def recommend(user_lat, user_lon, query, top_n=7):
    results = []
    for p in places:
        if isinstance(p["category"], str) and query.lower() in p["category"].lower():
            d = haversine(user_lat, user_lon, p["lat"], p["lon"])
            distance_score = max(0, 1 - d/10)
            popularity_score = p["popularity"] / 100
            score = (0.6 * popularity_score) + (0.4 * distance_score)
            results.append((score, p["name"], round(d,2), p["category"]))
    results.sort(key=lambda x: x[0], reverse=True)
    return results[:top_n]
