from request.response import response
import requests

class IMDb_request:
    API_KEY="k_5ih8v2uw"
    _base_url =f"https://www.google.com/"
    _base_url_ranking =f"https://imdb-api.com/en/API/Ratings/{API_KEY}"
    
        
    @classmethod
    def get_Movies(cls,Movie):
        res =  requests.get(cls._base_url+"/{}".format(Movie))
        return response(status_code=res.status_code, content=res.json(), cookie=res.cookies.get_dict())
    @classmethod
    def get_Ranking(cls,idMovie):
        res =  requests.get(cls._base_url_ranking+"/{}".format(idMovie))
        return response(status_code=res.status_code, content=res.json(), cookie=res.cookies.get_dict())
    @classmethod
    def get_data(cls,url):
        res = requests.get(cls.url)
        return response(status_code=res.status_code, content=res.json(), cookie=res.cookies.get_dict())