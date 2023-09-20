import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url=self.url
        response=requests.get(url)
        return response.content

    def load_json(self):
        data_list=[]
        data_hub = json.loads(self.get_response_body())
        for data in data_hub:
            data_dict = {"name": data["name"], "occupation": data["occupation"]}
            data_list.append(data_dict)
        return data_list
        pass

get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
# print(get_requester.get_response_body())
print(get_requester.load_json())