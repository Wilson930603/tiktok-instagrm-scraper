import scrapy,json,csv,os, requests, urllib
from os import path
class CrawlerSpider(scrapy.Spider):
    name = 'tiktok2'

    cookiesu = {
        'ttwid': '1%7CD7YbLSoS-WuQBhZnwzl3ydg8jVK5LhLOLpzOA90cABA%7C1688474448%7C6a9e4c16c5afe7e0780865faeb976a134fdd5797d8006e9a2d9c5474c9f0c258',
        'tt_chain_token': '/j0iCXuskNxaGiQicn+RYA==',
        '__tea_cache_tokens_1988': '{%22_type_%22:%22default%22%2C%22user_unique_id%22:%227250682842085869058%22%2C%22timestamp%22:1688181171318}',
        'tiktok_webapp_theme': 'light',
        'msToken': 'pLpNyl8QUZBqKZJwY5cl69NjVqIB4upnZo2DCnCshqjaPJTFKyWE7AFNSTgPs5SCMQfmYVOSgVS8F6o_2YNyh1ubCGFdDWalpu07MxxXSM9tMKVyVkuXDmOMnmf_RyXzExamfA50GHEt5CzB-rs=',
        'passport_csrf_token': '899d169317da00f0dc9b09347c2879d4',
        'passport_csrf_token_default': '899d169317da00f0dc9b09347c2879d4',
        'd_ticket': 'f433a1df61644289637165fa740f1578cb45a',
        'odin_tt': 'd5ee8be7bddae81c7c0c13090b7b4cd58301409fafe68be3e878be4ccff1b644d1cc6fc1e41f23ab45c41ab4f7883f5015a535be44f38149eab9f1fb3f4ffcb147ff976d2570f689b8abc7649c073a07',
        'cmpl_token': 'AgQQAPOFF-RO0rSfmLZsdt08_v4AkqITf4AOYM7DZQ',
        'passport_auth_status': 'ded31263a782c0ad7c9829b5612fa5a8%2C',
        'passport_auth_status_ss': 'ded31263a782c0ad7c9829b5612fa5a8%2C',
        'sid_guard': '9f6e75c0fa7c51dc31725b5ff170b67c%7C1688303151%7C15552000%7CFri%2C+29-Dec-2023+13%3A05%3A51+GMT',
        'uid_tt': 'f05bdc9de7d6d95ffd6bb7fca5399b9623d64c9dd4201093878a779f5bcc22ea',
        'uid_tt_ss': 'f05bdc9de7d6d95ffd6bb7fca5399b9623d64c9dd4201093878a779f5bcc22ea',
        'sid_tt': '9f6e75c0fa7c51dc31725b5ff170b67c',
        'sessionid': '9f6e75c0fa7c51dc31725b5ff170b67c',
        'sessionid_ss': '9f6e75c0fa7c51dc31725b5ff170b67c',
        'sid_ucp_v1': '1.0.0-KDg3ZGQwNGZmYmZlY2Y0N2UxMjhmMThjOTBhZTVmN2U0MjY0NDI5YjIKIAiFiJCinsLd0GQQr-yFpQYYswsgDDCu7IWlBjgCQOwHEAMaBm1hbGl2YSIgOWY2ZTc1YzBmYTdjNTFkYzMxNzI1YjVmZjE3MGI2N2M',
        'ssid_ucp_v1': '1.0.0-KDg3ZGQwNGZmYmZlY2Y0N2UxMjhmMThjOTBhZTVmN2U0MjY0NDI5YjIKIAiFiJCinsLd0GQQr-yFpQYYswsgDDCu7IWlBjgCQOwHEAMaBm1hbGl2YSIgOWY2ZTc1YzBmYTdjNTFkYzMxNzI1YjVmZjE3MGI2N2M',
        'store-idc': 'maliva',
        'store-country-code': 'vn',
        'store-country-code-src': 'uid',
        'tt-target-idc': 'alisg',
        'tt-target-idc-sign': 'Vf6PeWFHTpxssV-9cbu_Zv7an8A6mtlbxzXM2KE6BBEJjCXdPC8vbwr_IkkIs9AcLd0suzyEgfplWroFZAaAOdkMja8EvV1GAp-E9MkChrCeWjBfjvmhEyWZty_SJ4F6ALJ-f-uvkODllCduYvMNbTPgQ3zv9JNwZxcSv30ZOTQg12f35oQFB_sJQ192wnXC8FvkggDLW4FlyWb-4eiA4TXaPeMYhez_LWiUGfx36FPbco5UpqrLzFQP4w9r7-HJ--VtS5oQYZiuKREIuU-Q99GoMcHXzyi9f1RN_hPDemqdHEz1k9aqSSQQLQdgWelvY4ig0g_rdyXJtz-S1tjDLwB4vfX6iWWYDOPGqjIR2ht8vrzN_QdSRciAYghTVKwuASB93TZggCeu9NXCx7iEwEIyN98NHOID93E7MQ0ik8E0YKF97JnZRWFnQEE63rcmtx02cfWfNZUe0XI4mdSTGJ2JArz_zU-0n2tEqd049PTRCEb61WF7A9f9PEe1amWM',
        'tt_csrf_token': 'x8W4vh2Q-dKCg4nSgONlhz3xhLEHeOhiVQAw',
        'passport_fe_beating_status': 'true',
        's_v_web_id': 'verify_ljnygfo3_2LicBiRJ_ICbp_4ETl_80JC_m14sOHC4GR2Q',
        'msToken': 'lR2mBHPVyD6LBJUAmDbILtrhxKEn7w7T2ayeDEKfvc6GLcdaVuH8EXrhfmMUFTbS9KW3gSE0glaQGTFFxf_NrwSu8RTtkJRdIucWe3r_G-YgL6La6Iw-xxNRwlNEvpX0Bw_qtt3z9togUs3NXsI=',
    }

    headersu = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Connection': 'keep-alive',
        # 'Cookie': 'ttwid=1%7CD7YbLSoS-WuQBhZnwzl3ydg8jVK5LhLOLpzOA90cABA%7C1688474448%7C6a9e4c16c5afe7e0780865faeb976a134fdd5797d8006e9a2d9c5474c9f0c258; tt_chain_token=/j0iCXuskNxaGiQicn+RYA==; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227250682842085869058%22%2C%22timestamp%22:1688181171318}; tiktok_webapp_theme=light; msToken=pLpNyl8QUZBqKZJwY5cl69NjVqIB4upnZo2DCnCshqjaPJTFKyWE7AFNSTgPs5SCMQfmYVOSgVS8F6o_2YNyh1ubCGFdDWalpu07MxxXSM9tMKVyVkuXDmOMnmf_RyXzExamfA50GHEt5CzB-rs=; passport_csrf_token=899d169317da00f0dc9b09347c2879d4; passport_csrf_token_default=899d169317da00f0dc9b09347c2879d4; d_ticket=f433a1df61644289637165fa740f1578cb45a; odin_tt=d5ee8be7bddae81c7c0c13090b7b4cd58301409fafe68be3e878be4ccff1b644d1cc6fc1e41f23ab45c41ab4f7883f5015a535be44f38149eab9f1fb3f4ffcb147ff976d2570f689b8abc7649c073a07; cmpl_token=AgQQAPOFF-RO0rSfmLZsdt08_v4AkqITf4AOYM7DZQ; passport_auth_status=ded31263a782c0ad7c9829b5612fa5a8%2C; passport_auth_status_ss=ded31263a782c0ad7c9829b5612fa5a8%2C; sid_guard=9f6e75c0fa7c51dc31725b5ff170b67c%7C1688303151%7C15552000%7CFri%2C+29-Dec-2023+13%3A05%3A51+GMT; uid_tt=f05bdc9de7d6d95ffd6bb7fca5399b9623d64c9dd4201093878a779f5bcc22ea; uid_tt_ss=f05bdc9de7d6d95ffd6bb7fca5399b9623d64c9dd4201093878a779f5bcc22ea; sid_tt=9f6e75c0fa7c51dc31725b5ff170b67c; sessionid=9f6e75c0fa7c51dc31725b5ff170b67c; sessionid_ss=9f6e75c0fa7c51dc31725b5ff170b67c; sid_ucp_v1=1.0.0-KDg3ZGQwNGZmYmZlY2Y0N2UxMjhmMThjOTBhZTVmN2U0MjY0NDI5YjIKIAiFiJCinsLd0GQQr-yFpQYYswsgDDCu7IWlBjgCQOwHEAMaBm1hbGl2YSIgOWY2ZTc1YzBmYTdjNTFkYzMxNzI1YjVmZjE3MGI2N2M; ssid_ucp_v1=1.0.0-KDg3ZGQwNGZmYmZlY2Y0N2UxMjhmMThjOTBhZTVmN2U0MjY0NDI5YjIKIAiFiJCinsLd0GQQr-yFpQYYswsgDDCu7IWlBjgCQOwHEAMaBm1hbGl2YSIgOWY2ZTc1YzBmYTdjNTFkYzMxNzI1YjVmZjE3MGI2N2M; store-idc=maliva; store-country-code=vn; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=Vf6PeWFHTpxssV-9cbu_Zv7an8A6mtlbxzXM2KE6BBEJjCXdPC8vbwr_IkkIs9AcLd0suzyEgfplWroFZAaAOdkMja8EvV1GAp-E9MkChrCeWjBfjvmhEyWZty_SJ4F6ALJ-f-uvkODllCduYvMNbTPgQ3zv9JNwZxcSv30ZOTQg12f35oQFB_sJQ192wnXC8FvkggDLW4FlyWb-4eiA4TXaPeMYhez_LWiUGfx36FPbco5UpqrLzFQP4w9r7-HJ--VtS5oQYZiuKREIuU-Q99GoMcHXzyi9f1RN_hPDemqdHEz1k9aqSSQQLQdgWelvY4ig0g_rdyXJtz-S1tjDLwB4vfX6iWWYDOPGqjIR2ht8vrzN_QdSRciAYghTVKwuASB93TZggCeu9NXCx7iEwEIyN98NHOID93E7MQ0ik8E0YKF97JnZRWFnQEE63rcmtx02cfWfNZUe0XI4mdSTGJ2JArz_zU-0n2tEqd049PTRCEb61WF7A9f9PEe1amWM; tt_csrf_token=x8W4vh2Q-dKCg4nSgONlhz3xhLEHeOhiVQAw; passport_fe_beating_status=true; s_v_web_id=verify_ljnygfo3_2LicBiRJ_ICbp_4ETl_80JC_m14sOHC4GR2Q; msToken=lR2mBHPVyD6LBJUAmDbILtrhxKEn7w7T2ayeDEKfvc6GLcdaVuH8EXrhfmMUFTbS9KW3gSE0glaQGTFFxf_NrwSu8RTtkJRdIucWe3r_G-YgL6La6Iw-xxNRwlNEvpX0Bw_qtt3z9togUs3NXsI=',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }
    uniqueids=[]
    def start_requests(self):
        keyarray=['ai tools','author']
        for keywords in keyarray:
            path = "E:\\kco\\kevin\\"+keywords+"\\"
            os.chdir(path)
            for file in os.listdir():
                file_path = path+file
                f = open(file_path,encoding='utf8')
                Data = json.load(f)
                for item in Data['user_list']:
                    with open("E:\\kco\\kevin\\"+keywords+".txt") as file:
                        ulist = file.read()
                    lst = ulist.split("\n")
                    if item['user_info']['unique_id'] in lst:
                        continue
                    url="https://www.tiktok.com/@"+item['user_info']['unique_id']
                    # print(url)
                    yield scrapy.Request(url,callback=self.get_profile, headers=self.headersu,cookies=self.cookiesu,meta={'keywords':keywords,'uniqueId':item['user_info']['unique_id']}, dont_filter=True)
    def get_profile(self,response):
        html = response.text.split('<script id="SIGI_STATE" type="application/json">')[1].split('</script>')[0]
        Data=json.loads(html)
        keywords=response.meta['keywords']
        url=response.url
        uniqueid=response.meta['uniqueId']
        nickname=Data['UserModule']['users'][uniqueid]['nickname']
        following=Data['UserModule']['stats'][uniqueid]['followingCount']
        followers=Data['UserModule']['stats'][uniqueid]['followerCount']
        likes=Data['UserModule']['stats'][uniqueid]['heartCount']
        signature=Data['UserModule']['users'][uniqueid]['signature']
        videoCount=Data['UserModule']['stats'][uniqueid]['videoCount']
        with open("E:\\kco\\kevin\\"+keywords+'.csv', 'a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([url, uniqueid, nickname, following, followers, likes, signature,videoCount])
        open("E:\\kco\\kevin\\"+keywords+'.txt','a',encoding='utf-8').write(uniqueid+"\n")
        # print(Data['UserModule']['users'][uniqueId]['nickname'])