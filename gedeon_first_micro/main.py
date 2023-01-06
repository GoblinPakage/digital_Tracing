import logging
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Blockchain"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')


from flask import render_template
from flask import Flask
from reqData.get_request import get_request
from reqData.textScript import *
from reqData.decoration import exectionTime_decoration
from reqData.helloAnalytics import helloAnalytics


app = Flask(__name__, static_url_path='/static',
            static_folder='static',
            template_folder='templates')




@app.route('/', methods=["GET"])
def hello_world():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=UA-250921816-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-250921816-1');
    </script>
    """
    return prefix_google + render_template('index.html', name="Word")

@app.route('/logger', methods=["GET"])
def logger():
    
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=UA-250921816-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', ' UA-250921816-1');
    </script>
    """

    '''     logging.debug("This is debug")
    logging.info("This is info")
    
    logging.error("This is error")
    logging.critical("This is critical") '''
    
    logging.debug("This is warning")
    print(logging.debug("This is warning"))
    return prefix_google + render_template('logger.html', value='This is warning')



@app.route('/cookie', methods=["GET","POST"])
def func_cookie():
   # with app.app_context():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=UA-250921816-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', ' UA-250921816-1');
    </script>
    """
    #req=requests.get('https://www.google.com')
    #cookie=req.cookies.get_dict()
    res=get_request.get_data('https://www.google.com')
    res2=get_request.get_data("https://analytics.google.com/analytics/web/#/report-home/a250921816w345128286p281212475")
    logging.debug("this a debbug log")
    print("here we try to debbug")


    # Define the auth scopes to request.
    scope = 'https://www.googleapis.com/auth/analytics.readonly'
    key_file_location = 'client_secrets.json'

    # Authenticate and construct service.
    service = helloAnalytics.get_service(
            api_name='analytics',
            api_version='v3',
            scopes=[scope],
            key_file_location=key_file_location)

    #profile_id = helloAnalytics.get_first_profile_id(service)
    helloAnalytics.print_results(helloAnalytics.get_results(service, '281212475')) #here is the id of the view
    #data=helloAnalytics.get_results(service, profile_id) this can't be use for the id of profile
    data=helloAnalytics.get_results(service, '281212475')
    evt=data.get('rows')[0][0]
    vist=data.get('rows')[0][1]
    return prefix_google + render_template('cookie.html', value=res.cookie, analytic=res2.text, event= evt, visit= vist)



@exectionTime_decoration
@app.route('/Bar chart', methods=["GET"])
def chart_request():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=UA-250921816-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-250921816-1');
    </script>
    """
    #data= pytrends.interest_over_time()
    #data.to_csv(path_or_buf='../static/time.csv')
    return prefix_google + render_template('chart.html', name="bar chart")


@exectionTime_decoration
@app.route('/Comparaison', methods=["GET"])
def comparaison():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=UA-250921816-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-250921816-1');
    </script>
    """
    req=get_request.get_data('https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt')
    data=req.text
    dict_count=Count_Word_UsingDict(data)
    #funct_count=Count_Word_UsingCounterfunc(data)
    
    return prefix_google + render_template('comparaison.html', D_count=dict_count, F_count="Function Count_Word_UsingDict Execution time is 8.999999998593466e-03 seconds")   