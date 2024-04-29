import scrapy,json,re,os,platform,time,requests,urllib3,random
from crawldata.functions import *
from datetime import datetime
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class CrawlerSpider(scrapy.Spider):
    name = 'instagram'
    DATE_CRAWL=datetime.now().strftime('%Y-%m-%d')
    #custom_settings={'LOG_FILE':'./log/'+name+'_'+DATE_CRAWL+'.log'}
    if platform.system()=='Linux':
        URL='file:////' + os.getcwd()+'/scrapy.cfg'
    else:
        URL='file:///' + os.getcwd()+'/scrapy.cfg'
    KEYWORDS=[]
    if os.path.exists('keywords.txt'):
        KEYWORDS=re.split('\r\n|\n',open('keywords.txt').read())
    username=''
    password=''
    def __init__(self, username='',password='', **kwargs):
        if username:
            self.username=username
        if password:
            self.password=password
        super().__init__(**kwargs)
    def start_requests(self):
        yield scrapy.Request(self.URL,callback=self.parse,dont_filter=True)
    def parse(self, response):
        if self.username!='' and self.password!='':
            RES=requests.Session()
            link='https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='
            login_url = 'https://www.instagram.com/accounts/login/ajax/'
            dtime = int(datetime.now().timestamp())
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','TE': 'Trailers',}
            response = RES.get(link,headers=headers,verify=False)
            cookies=response.cookies.get_dict()
            csrf=cookies['csrftoken']
            payload = {'username': self.username,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{dtime}:{self.password}','queryParams': {},'optIntoOneTap': 'false'}
            login_header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36","X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","x-csrftoken": csrf}
            login_response = RES.post(login_url, data=payload, headers=login_header,verify=False,cookies=cookies)
            json_data = json.loads(login_response.text)
            if 'status' in json_data and json_data['status']=='ok':
                print("login successful")
                cookiess = login_response.cookies
                cookie_jar = cookiess.get_dict()
                cookies.update(cookie_jar)
                for keyword in self.KEYWORDS:
                    data = {'lsd': 'xJ1VKd5UDN6RRfcy-vZNO_','fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'PolarisSearchBoxRefetchableQuery','variables': '{"data":{"context":"blended","include_reel":"true","query":"'+keyword+'","rank_token":"","search_surface":"web_top_search"}}','doc_id': '6171346942983319'}
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0','Accept': '*/*','Accept-Language': 'en-GB,en;q=0.5','Content-Type': 'application/x-www-form-urlencoded','X-FB-Friendly-Name': 'PolarisSearchBoxRefetchableQuery','X-CSRFToken': csrf,'X-IG-App-ID': '936619743392459','X-FB-LSD': 'xJ1VKd5UDN6RRfcy-vZNO_','X-ASBD-ID': '129477','Origin': 'https://www.instagram.com','Alt-Used': 'www.instagram.com','Connection': 'keep-alive','Referer': 'https://www.instagram.com/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin'}
                    response = RES.post('https://www.instagram.com/api/graphql', cookies=cookies, headers=headers, data=data)
                    DATA=json.loads(response.text)
                    Data=DATA['data']['xdt_api__v1__fbsearch__topsearch_connection']['users']
                    for row in Data:
                        print(row)
                        url='https://www.instagram.com/api/v1/users/web_profile_info/?username='+row['user']['username']
                        cookies_detail = {'dpr': '1.25','ig_did': '01FA2C57-CAAE-4028-9A2F-4DFD94167F28','datr': 'hZShZO9aMMMwxef9256U-GBB','csrftoken': csrf,'mid': 'ZKGUhgALAAEckowTAE5wJQXBWACr','ig_nrcb': '1','ds_user_id': '48302235355','shbid': '977\\05448302235355\\0541719847035:01f7a9eba2904bc1516de6731ecefaccf365cb3ecbee3052d3f2dfd418a1636bdb7a6f00','shbts': '1688311035\\05448302235355\\0541719847035:01f735dbb685bce34f7d57bd503093ac682ebc0f006274428bff1016b5cfe2a4e2f32fbd','rur': 'NHA\\05448302235355\\0541719901087:01f7093aba827d1aa6c7d333f1f5e4c8a7c71b8b93b1672d81013b5006ee3a2e82eb9383','sessionid': '48302235355^%^3A0rSYZQkQRaf90j^%^3A21^%^3AAYcFD9SThWOKOh-qWMtDibUyGh3wPrVr4jwiA94MzQ'}
                        headers_detail = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0','Accept': '*/*','Accept-Language': 'en-GB,en;q=0.5','X-CSRFToken': csrf,'X-IG-App-ID': '936619743392459','X-ASBD-ID': '129477','X-IG-WWW-Claim': 'hmac.AR25pmmtHqqpHDYgSBW87eJQvONw2tAaM02BHbgKzUCPm-mJ','X-Requested-With': 'XMLHttpRequest','Alt-Used': 'www.instagram.com','Connection': 'keep-alive','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin'}
                        print('\n ----------------\n',url)
                        headers_detail['Referer']='https://www.instagram.com/'+row['user']['username']+'/'
                        response = RES.get(url, cookies=cookies_detail, headers=headers_detail)
                        Data_profile=json.loads(response.text)
                        rs=Data_profile['data']['user']
                        item={}
                        item['search key']=keyword
                        item['username']=rs['username']
                        item['Full name']=rs['full_name']
                        try:
                            item['Number of posts']=rs['edge_owner_to_timeline_media']['count']
                        except:
                            item['Number of posts']=''
                        try:
                            item['Folowers count']=rs['edge_followed_by']['count']
                        except:
                            item['Folowers count']=''
                        try:
                            item['Folowing count']=rs['edge_follow']['count']
                        except:
                            item['Folowing count']=''
                        item['url']='https://www.instagram.com/'+item['username']+'/'
                        biography=rs.get('biography','')
                        email=re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", biography)
                        emails=[]
                        for em in email:
                            if not em in emails:
                                emails.append(em)
                        item['Email']=', '.join(emails)
                        item['Boi']=biography
                        item['External url']=rs['external_url']
                        yield(item)
                        time.sleep(random.randrange(5,10))