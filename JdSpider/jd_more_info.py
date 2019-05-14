import json
import os
import re

import requests
from lxml import etree


class JSpider(object):
    def __init__(self, cookie):
        self.session = requests.session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
        cookie_dict = {}
        list = cookie.split(';')
        for i in list:
            try:
                cookie_dict[i.split('=')[0]] = i.split('=')[1]
            except IndexError:
                cookie_dict[''] = i
        requests.utils.add_dict_to_cookiejar(self.session.cookies, cookie_dict)

    # 个人信息
    def get_user_info(self):
        url = 'https://wq.jd.com/user/info/QueryXBCreditScore?_=1556338705353&sceneval=2&g_login_type=1&callback=getCreditInfoCb&g_tk=2127038752&g_ty=ls'
        self.headers['Referer'] = 'https://wqs.jd.com/my/asset.html'
        resp = self.session.get(url, headers=self.headers).content.decode().replace('try{getCreditInfoCb(', '').replace(
            ');}catch(e){}', '')

        json_data = json.loads(resp)['data']
        url = 'https://api.m.jd.com/api?appid=pc_home_page&functionId=getBaseUserInfo&loginType=3'
        resp = json.loads(self.session.get(url, headers=self.headers).content.decode())['returnObj']
        json_data.append(resp)
        str = json.dumps(json_data)
        self.write_json('user_info.json', str)

    def write_json(self, name, str):
        file_path = os.path.join(os.path.dirname(__file__) + '/' + name)
        with open(file_path, 'w') as f:
            f.write(str)

    # 信用账单
    def get_creditData(self):
        url = 'https://trade.jr.jd.com/async/creditData.action'
        resp = self.session.get(url, headers=self.headers)
        self.write_json('creditData.json', resp.content.decode())

    # 钱包概括
    def get_browseDataNew(self):
        url = 'https://trade.jr.jd.com/async/browseDataNew.action'
        resp = self.session.get(url)
        self.write_json('wallet.json', resp.content.decode())

    # 收益账单
    def get_income(self):
        url = 'https://trade.jr.jd.com/centre/getOverviewInData.action'
        resp = self.session.get(url)
        self.write_json('income.json', resp.content.decode())

    # 地址
    def get_addr(self):
        url = 'https://easybuy.jd.com/address/getEasyBuyList.action'
        headers = {
            'Host': 'easybuy.jd.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Referer': 'https://home.jd.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }
        resp = self.session.get(url, headers=headers)
        obj_list = etree.HTML(resp.content.decode()).xpath('//div[@class="item-lcol"]')
        json_list = []
        for obj in obj_list:
            item = {}
            item['name'] = obj.xpath('./div[1]/div[1]/text()')[0].strip()
            item['addr'] = obj.xpath('./div[2]/div[1]/text()')[0].strip()
            item['detail_addr'] = obj.xpath('./div[3]/div[1]/text()')[0].strip()
            item['mobile'] = obj.xpath('./div[4]/div[1]/text()')[0].strip()
            item['tel'] = obj.xpath('./div[5]/div[1]/text()')[0].strip()
            item['email'] = obj.xpath('./div[6]/div[1]/text()')[0].strip()
            json_list.append(item)
        self.write_json('addr.json', json.dumps(json_list))

    # 银行卡
    def get_YHK(self):
        url = 'https://authpay.jd.com/card/queryBindCard.action'
        resp = self.session.get(url, headers=self.headers)
        item = {}
        item['name'] = etree.HTML(resp.content.decode()).xpath('//span[contains(text(),"持卡人姓名")]/text()')[0].replace(
            '持卡人姓名：', '')
        item['mobile'] = etree.HTML(resp.content.decode()).xpath('//span[contains(text(),"手机号：")]/text()')[0].replace(
            '手机号：', '')
        item['last_num'] = etree.HTML(resp.content.decode()).xpath('//span[contains(text(),"尾号")]/text()')[0].replace(
            '尾号', '')
        str = json.dumps(item)
        self.write_json('YHK_info.json', str)

    # 小金库账单
    def get_xjk_info(self):
        url = 'https://xjk.jr.jd.com/gold/account'
        resp = self.session.get(url)
        self.write_json('xjk.json', resp.content.decode())

    # 理财收益
    def get_finance_income(self):
        url = 'https://trade.jr.jd.com/ajaxFinance/queryFundInfo.action'
        resp = self.session.get(url)
        self.write_json('finance_income.json', resp.content.decode())

    # 钢镚数
    def get_GB_num(self):
        url = 'https://gb.jd.com/asset/myassets.html?from=myzc-left-gb'
        resp = self.session.get(url)
        num = etree.HTML(resp.content.decode()).xpath('//em[@class="h-i-num"]/text()')[0]
        str = json.dumps({'gb_num': num})
        self.write_json('GB_num.json', str)

    # 京东金融交易单
    def get_JY_bill(self):
        # 可获取多页，定义pageNo
        url = 'https://trade.jr.jd.com/trade/tradebuynew.action?pageNo=0&pageSize=10&timeFlag=0&projectType=0&orderStatus=-1&date1=&date2='
        resp = self.session.get(url, headers=self.headers)
        self.write_json('jiaoyi_bill.json', resp.content.decode())

    # 收藏店铺
    def get_follow_shops(self):
        url = 'https://t.jd.com/follow/vender'
        resp = self.session.get(url)
        ele = etree.HTML(resp.content.decode())
        obj_list = ele.xpath('//div[@class="mf-shop-list "]/div')
        json_list = []
        for obj in obj_list:
            item = {}
            item['name'] = ''.join(obj.xpath('.//div[@class="shop-name"]//text()')).strip()
            item['url'] = obj.xpath('.//div[@class="shop-name"]/a/@href')[0]
            json_list.append(item)
        str = json.dumps(json_list)
        self.write_json('follow_shops.json', str)

    # 收藏s商品
    def get_follow_products(self):
        url = 'https://t.jd.com/follow/product'
        resp = self.session.get(url)
        ele = etree.HTML(resp.content.decode())
        obj_list = ele.xpath('//div[@class="mf-goods-list clearfix "]/div')
        json_list = []
        for obj in obj_list:
            item = {}
            item['name'] = ''.join(obj.xpath('.//div[@class="p-name"]//text()')).strip()
            item['url'] = obj.xpath('.//div[@class="p-name"]/a/@href')[0]
            item['price'] = ''.join(obj.xpath('.//div[@class="p-price"]/strong/@price')).strip()
            item['status'] = ''.join(obj.xpath('.//div[@class="p-stats"]//text()')).strip()
            json_list.append(item)
        str = json.dumps(json_list)
        self.write_json('follow_products.json', str)

    # 收藏s商品
    def get_cart(self):
        url = 'https://cart.jd.com/cart.action'
        resp = self.session.get(url)
        ele = etree.HTML(resp.content.decode())
        obj_list = ele.xpath('//div[@class="item-form"]')
        json_list = []
        for obj in obj_list:
            item = {}
            item['name'] = ''.join(obj.xpath('.//div[@class="p-name"]//text()')).strip()
            item['skus'] = ''.join(obj.xpath('.//div[@class="cell p-props p-props-new"]//text()')).strip()
            item['url'] = obj.xpath('.//div[@class="p-name"]/a/@href')[0]
            item['price'] = ''.join(obj.xpath('.//div[@class="cell p-sum"]//text()')).strip()
            item['num'] = ''.join(obj.xpath('.//div[@class="cell p-quantity"]//input/@value')).strip()
            json_list.append(item)
        str = json.dumps(json_list)
        self.write_json('carts.json', str)

    # 已购商品
    def get_orders(self):
        for i in [2019, 2018]:
            url = 'https://order.jd.com/center/list.action?search=0&d={}&s=4096'.format(i)
            resp = self.session.get(url)
            ele = etree.HTML(resp.content.decode('gbk'))
            obj_list = ele.xpath('//table[@class="td-void order-tb"]/tbody')[1:]
            json_list = []
            url = 'https://order.jd.com/lazy/getOrderProductInfo.action'
            try:
                data = {
                    'orderWareIds': '{}'.format(
                        re.findall(r"ORDER_CONFIG\['orderWareIds'\]='([\d,]+)'", resp.content.decode('gbk'))[0]),
                    'orderWareTypes': '{}'.format(
                        re.findall(r"ORDER_CONFIG\['orderWareTypes'\]='([\d,]+)'", resp.content.decode('gbk'))[0]),
                    'orderIds': '{}'.format(
                        re.findall(r"ORDER_CONFIG\['orderIds'\]='([\d,]+)'", resp.content.decode('gbk'))[0]),
                    'orderTypes': '{}'.format(
                        re.findall(r"ORDER_CONFIG\['orderTypes'\]='([\d,]+)'", resp.content.decode('gbk'))[0]),
                    'orderSiteIds': '{}'.format(
                        re.findall(r"ORDER_CONFIG\['orderSiteIds'\]='([\d,]+)'", resp.content.decode('gbk'))[0]),
                    'sendPays': '{}'.format(
                        re.findall(r"ORDER_CONFIG\['sendPays'\]='([\d,]+)'", resp.content.decode('gbk'))[0]),
                }
            except Exception:
                return
            json_list = json.loads(self.session.post(url, data=data).content.decode('gbk'))
            ret_list = []
            for obj in obj_list:
                try:
                    item = json_list[obj_list.index(obj)]
                    item['goods-number'] = ''.join(obj.xpath('.//div[@class="goods-number"]//text()')).strip()
                    item['consignee tooltip'] = ''.join(obj.xpath('.//div[@class="consignee tooltip"]/text()')).strip()
                    item['amount'] = ''.join(obj.xpath('.//div[@class="amount"]//text()')).strip()
                    item['order-shop'] = ''.join(obj.xpath('.//span[@class="order-shop"]//text()')).strip()
                    ret_list.append(item)
                except Exception:
                    continue

            self.write_json('jd_orders_{}.json'.format(i), json.dumps(ret_list))

        # dict = {
        #     "orderType": 37,
        #     "erpOrderId": "%s"
        # }
        #
        # obj_list = [{"orderType": 37, "erpOrderId": "%s" % (i.replace('tb-', ''))} for i in
        #             ele.xpath('//table[@class="td-void order-tb"]/tbody/@id')]
        #
        # url = 'https://ordergw.jd.com/orderCenter/app/1.0/?queryList={}'.format(json.dumps(obj_list))
        # result_resp = self.session.get(url, headers=self.headers).content.decode().replace('null(', '')[:-1]


if __name__ == '__main__':
    cookie = 'shshshfpa=7da97119-ca02-a4b5-f883-70bffbb95d2d-1551953689; shshshfpb=oMWkS2uhzSRpZkjikQcMliQ%3D%3D; PCSYCityID=904; areaId=12; ipLoc-djd=12-965-967-38496; user-key=c2b0ef35-0281-4be2-bcf4-4148cb7f518c; sid=509cf3bcff856462fbf0d27defc956e5; __jdu=1551953690075275239163; cn=2; mt_xid=V2_52007VwMWVl1QVlgYQRhdA2MAFFZeWlpaGEspCAFjA0ZUXVBODx4cG0AAMlRFTlVQAA0DHB8MUDJQEAdcXgdTL0oYXA17AhdOXlBDWRxCHV0OZQUiUm1YYlgYTRFeAGYDGmJfXFNf; TrackID=15Z7AWYzc3eAvMsE9Og3XV9Vqvs8o3ajKGACHAWtDTYe7ivuULPCSkMo9tWJS9lHXwCZ8LdfUDyXQ3mWG_bQVpmsyOSMbH2Pp27E7FkLg140GREw3XL6HXu6C6fcCcMXL; __jda=122270672.1551953690075275239163.1551953690.1556614926.1557023684.18; __jdc=122270672; __jdv=122270672|baidu|-|organic|not set|1557023684472; shshshfp=4e62136f3f0d1f33c8191339402dd3a2; thor=BF23B370DD491EEE15CB4D3DBB29B61D6F15B23D58582409C58B0131D8A52E7B2A06114EC2F615519BB1B4EF9CC199A07E6CE4B2E82A125954D7C292D5F544DE013BB9CC77B3B4756CB9125C1021395832FFA1913E13F06D3D1F9ACF727A228E96D03B8E2FFAED7952795D7D31A24E79D58C916331895A6F660C9D84B083319A88C75EED9A114DC7D913A8DD9F83A466; pinId=PFNaS1XmeXF9TBCvJEIlnw; pin=18621759441_p; unick=jd_Miss+Vivi; ceshi3.com=000; _tp=s3iKj%2BxpTSF0rzuw4y6G4g%3D%3D; _pst=18621759441_p; shshshsID=a2fc2b444f7cc5ec786568326575de27_2_1557023849318; 3AB9D23F7A4B3C9B=Z2QEKJIHVKXOC2JNFZIJKKVZ5XVWWIJWQ5TRJ7BOO4K45QVTUZKRK4WXVBSIP5WQ7ZQYP22ZTJWGQILVDNH7G7QGDA; __jdb=122270672.6.1551953690075275239163|18.1557023684'
    spider = JSpider(cookie)
    spider.get_orders()
    # spider.get_creditData()
    # spider.get_browseDataNew()
    # spider.get_income()
    # spider.get_user_info()
    # spider.get_addr()
    # spider.get_YHK()
    # spider.get_xjk_info()
    # spider.get_finance_income()
    # spider.get_GB_num()
    # spider.get_JY_bill()
    # spider.get_follow_shops()
    # spider.get_follow_products()
    # spider.get_cart()
