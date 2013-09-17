from flask import Flask
from flask.templating import render_template
from vendors.yandex_dns.api import YandexDnsApi


app = Flask(__name__)

a = YandexDns()

@app.route('/')
def hello_world():
    
    # yandex_dns_api = Yan
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
