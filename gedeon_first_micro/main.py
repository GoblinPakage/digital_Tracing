from flask import Flask
from request.request import IMDb_request
import logging
from flask import render_template
import requests

app = Flask(__name__)

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
    gtag('config', ' UA-250921816-1');
    </script>
    """
    return prefix_google + render_template('index.html', name="Home")

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
    
    logging.warning("This is warning")
    #print(log)
    return prefix_google + render_template('logger.html', value='Watch out!')

@app.route('/cookie', methods=["GET"])
def cookie():
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
        res=IMDb_request.get_data(url=f"https://www.google.com/")
        res2=IMDb_request.get_data(f"https://analytics.google.com/analytics/web/#/report-home/a250921816w345128286p281212475")

        return prefix_google + render_template('cookie.html', value=res.cookie, analytic=res2.content)
