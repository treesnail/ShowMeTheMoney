__author__ = 'zdz'
import tushare as ts
import urllib2
from BeautifulSoup import BeautifulSoup


def get_gp_code():
    gp_all = ts.get_today_all()
    gp_code = list(gp_all['code'].values)
    return gp_code

def create_gp_url():
    gp_code = get_gp_code()
    url_tmp ='http://data.eastmoney.com/zjlx/'
    gp_url = [url_tmp + str(gp_code[i]) + '.html'for item in range(1)]
    return gp_url

def get_one_gp(url_tmp):
    response = urllib2.urlopen(url_tmp)
    html_tmp = response.read()
    return html_tmp

def analysis_html(html_tmp):
    soup = BeautifulSoup(html_tmp)


