from reqData.response import response
import requests

class get_request:
    API_KEY="k_5ih8v2uw"
    _base_url =f"https://www.google.com/"
    _base_url_ranking =f"https://imdb-api.com/en/API/Ratings/{API_KEY}"
    
        
    '''     @classmethod
    def get_Movies(cls,Movie):
        res =  requests.get(cls._base_url+"/{}".format(Movie))
        return response(status_code=res.status_code, content=res.json(), cookie=res.cookies.get_dict())
    @classmethod
    def get_Ranking(cls,idMovie):
        res =  requests.get(cls._base_url_ranking+"/{}".format(idMovie))
        return response(status_code=res.status_code, content=res.json(), cookie=res.cookies.get_dict()) '''
    #@classmethod
    def get_data(url):
      
        req = requests.get(url)
        return response(status_code=req.status_code, text=req.text, cookie=req.cookies.get_dict())