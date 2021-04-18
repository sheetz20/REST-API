import requests
import pprint
import pandas as pd

api_key = "enter api key here"
api_key_v4 = "enter api key for v4"


"""
Endpoint
GET
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key={api_key}
"""

#using v3
movie_id = 550
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
# endpoint_path = f"/movie/{movie_id}"
endpoint_path = f"/search/movie"
search_query = "Endgame"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
# print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.json())
if r.status_code in range(200,299):
    data = r.json()
    results = data['results']
    # print(results[0].keys())
    # print(results)
    if len(results) > 0:
        movie_ids = set()
        for result in results:
            _id = result['id']
            movie_ids.add(_id)
        # print(list(movie_ids))
output = "movies.csv"
movie_data = []

for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint_path = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint_path)
    if r.status_code in range(200,299):
        data = r.json()
        movie_data.append(data)
    # print(movie_data)

df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output,index=False)



#using v4
# movie_id = 550
# api_version = 4
# api_base_url = f"https://api.themoviedb.org/{api_version}"
# endpoint_path = f"/movie/{movie_id}"
# headers = {
#     'Authorization': f'Bearer {api_key_v4}',
#     'Content-Type': 'application/json;charset=utf-8'
# }
# endpoint = f"{api_base_url}{endpoint_path}"
#
# r = requests.get(endpoint,headers=headers)

# print(r.status_code)
# print(r.text)