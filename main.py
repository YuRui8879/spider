import requests
from bs4 import BeautifulSoup
import re
import time

def login(username,password):
    url = 'https://cas.bjut.edu.cn/login?service=https%3A%2F%2Fmy.bjut.edu.cn%2Fc%2Fportal%2Flogin'
    # params = {
    #     'service':'https://my.bjut.edu.cn/c/portal/login'
    # }
    strhtml = requests.get(url, verify=False)
    soup = BeautifulSoup(strhtml.text, features="html.parser")
    lt = soup.find_all(name='input', attrs={'name': 'lt'})
    lt = lt[0]['value']
    exe = soup.find_all(name='input', attrs={'name': 'execution'})
    exe = exe[0]['value']

    post_data = {
        'username': str(username),
        'password': str(password),
        'lt': str(lt),
        '_eventId': 'submit',
        'submit': '',
        'execution': str(exe)
    }
    strhtml = requests.post(url, data=post_data, verify=False)
    # print(strhtml.request.headers)
    cookie = strhtml.request.headers['Cookie']
    return cookie

def index_html(cookie):
    url = 'https://my.bjut.edu.cn/group/graduate/index?p_p_id=bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK&p_p_lifecycle=0&p_p_state=pop_up&p_p_mode=view&p_p_col_id=column-5&p_p_col_count=3&_bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK_action=listMore'
    params = {
        'p_p_id': 'bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK',
        'p_p_lifecycle': '0',
        'p_p_state': 'pop_up',
        'p_p_mode': 'view',
        'p_p_col_id': 'column-5',
        'p_p_col_count': '3',
        '_bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK_action': 'listMore'
    }
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'my.bjut.edu.cn',
        'Referer': 'https://my.bjut.edu.cn/group/graduate/index?ticket=ST-9832132-ZX1fGTfgz3pBNYIlXuCZ-cas.bjut.edu.cn',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Cookie': cookie
    }
    strhtml = requests.get(url, params=params, headers=header, verify=False)
    cookie = strhtml.request.headers['Cookie']
    return cookie

def notification_html(cookie,index):
    url = 'https://my.bjut.edu.cn/group/graduate/index?p_p_id=bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK&p_p_lifecycle=0&p_p_state=exclusive&p_p_mode=view&_bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK_action=listMoreAjaxQuery&sEcho=1&iColumns=3&sColumns=title%2Cpublis_dept%2Cpublished&iDisplayStart='+str(index*25)+'&iDisplayLength=25&mDataProp_0=title&sSearch_0=&bRegex_0=false&bSearchable_0=true&bSortable_0=false&mDataProp_1=publis_dept&sSearch_1=&bRegex_1=false&bSearchable_1=false&bSortable_1=false&mDataProp_2=published&sSearch_2=&bRegex_2=false&bSearchable_2=false&bSortable_2=false&sSearch=&bRegex=false&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&_=0000000000000'
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'my.bjut.edu.cn',
        'Referer': 'https://my.bjut.edu.cn/group/graduate/index?p_p_id=bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK&p_p_lifecycle=0&p_p_state=pop_up&p_p_mode=view&p_p_col_id=column-5&p_p_col_count=3&_bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK_action=listMore',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cookie
    }
    params = {
        'p_p_id': 'bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK',
        'p_p_lifecycle': '0',
        'p_p_state': 'exclusive',
        'p_p_mode': 'view',
        '_bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK_action': 'listMoreAjaxQuery',
        'sEcho': '1',
        'iColumns': '3',
        'sColumns': 'title,publis_dept,published',
        'iDisplayStart': str(index*25),
        'iDisplayLength': '25',
        'mDataProp_0': 'title',
        'sSearch_0': '',
        'bRegex_0': 'false',
        'bSearchable_0': 'true',
        'bSortable_0': 'false',
        'mDataProp_1': 'publis_dept',
        'sSearch_1': '',
        'bRegex_1': 'false',
        'bSearchable_1': 'false',
        'bSortable_1': 'false',
        'mDataProp_2': 'published',
        'sSearch_2': '',
        'bRegex_2': 'false',
        'bSearchable_2': 'false',
        'bSortable_2': 'false',
        'sSearch': '',
        'bRegex': 'false',
        'iSortCol_0': '0',
        'sSortDir_0': 'asc',
        'iSortingCols': '1',
        '_': '0000000000000'
    }
    strhtml = requests.get(url, params=params, headers=header, verify=False)
    cookie = strhtml.request.headers['Cookie']
    return strhtml,cookie

def get_wid_and_ref(strhtml):
    dichtml = eval(strhtml.text)['aaData']
    res = []

    regrex_title = re.compile(r'title=\'(.*)\' ')
    regrex_wid = re.compile(r'\(\'.*\'\)')
    regrex_href = re.compile((r'href=\'.*\''))
    for data in dichtml:
        item = {'title': '', 'time': '', 'publis_dept': '', 'wid': '', 'href': ''}
        title = regrex_title.search(data['title']).group().split('\'')[1]
        try:
            item['wid'] = regrex_wid.search(data['title']).group().split('\'')[1]
        except Exception as e:
            item['href'] = regrex_href.search(data['title']).group().split('\'')[1]
        item['title'] = title
        item['time'] = data['published']
        item['publis_dept'] = data['publis_dept']
        res.append(item)
    return res

def wid_html(cookie,wid):
    url = 'https://my.bjut.edu.cn/group/graduate/index?p_p_id=bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK&p_p_lifecycle=0&p_p_state=pop_up&p_p_mode=view&_bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK_action=browse&wid'+wid
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'my.bjut.edu.cn',
        'Referer': 'https://my.bjut.edu.cn/group/graduate/index?p_p_id=bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK&p_p_lifecycle=0&p_p_state=pop_up&p_p_mode=view&p_p_col_id=column-5&p_p_col_count=3&_bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK_action=listMore',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User':'?1',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cookie
    }
    params = {
        'p_p_id': 'bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK',
        'p_p_lifecycle': '0',
        'p_p_state': 'pop_up',
        'p_p_mode': 'view',
        '_bulletinListForCustom_WAR_infoDiffusionV2portlet_INSTANCE_JfzAjYUtKgzK_action': 'browse',
        'wid':wid
    }
    strhtml = requests.get(url, params=params, headers=header, verify=False)
    soup = BeautifulSoup(strhtml.text,features="html.parser")
    soup = soup.find(name='div',attrs={'class':'news-cr uecontent'})
    content = []
    for child in soup.children:
        if child.name == 'p':
            content.append(analysis_text(child))
        elif child.name == 'table':
            content.extend(analysis_table(child.tbody.children))
    return content

def href_html(href):
    url = href
    header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'portal2nd.bjut.edu.cn',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    strhtml = requests.get(url, headers=header, verify=False)
    strhtml.encoding = 'utf-8'
    soup = BeautifulSoup(strhtml.text, features="html.parser")
    soup = soup.find('div',attrs={'class':'zhengwen'})
    res = []
    try:
        for child in soup.children:
            if child.name == 'p':
                res.append(analysis_text(child))
            elif child.name == 'table':
                res.extend(analysis_table(child.tbody.children))
    except:
        pass
    print(res)


def analysis_text(a):
    txt = a.get_text()
    return txt + '\n'

def analysis_table(a):
    res = []
    reg = re.compile(("<[^>]*>"))  # 清除html标签,提取文本
    row0 = []  # row0用于保存上一行的信息
    flag = True  # row0未初始化
    for child in a:
        row = []  # 保存表格提取结果
        if child.find('th'):  # 提取表格字段
            for value in child.children:
                st = reg.sub('', str(value))  # 正则匹配替换
                row.append((st.strip('\n')))
            row = '  |  '.join(row)
            res.append(row+'\n')
            continue
        if child.find('td'):  # 提取每一行
            while child.find('sup'):  # 先清洗可能存在的上标符号
                child.find('sup').extract()
            for value in child.children:
                st = reg.sub('', str(value))
                row.append(st.strip('\n'))
            if flag:
                flag = False
            if len(row) < len(row0):  # 与上一行比较,分析是否需要处理字段缺省的情况
                row_temp = row0[0:len(row0) - len(row)]
                for i in range(len(row)):
                    row_temp.append(row[i])
                row0 = row_temp
                row_temp = '  |  '.join(row_temp)  # 将列表保存的字段连接起来
                res.append(row_temp + '\n')
                continue
            row0 = row
            row = '  |  '.join(row)
            res.append(row + '\n')
    return res

def select_notification(dic,cookie,sels):
    content = []
    for item in dic:
        if not item['time'] == time.strftime("%Y-%m-%d", time.localtime()):
            continue
        else:
            for sel in sels:
                if sel in item['title']:
                    if not item['wid'] == '':
                        content.append(wid_html(cookie, item['wid']))
                    else:
                        content.append(href_html(item['href']))
    return content



if __name__ == '__main__':
    name = ''
    password = ''
    strhtml,cookie = notification_html(index_html(login(name,password)),0)
    dic = get_wid_and_ref(strhtml)
    content = select_notification(dic,cookie,['竞赛','比赛','停电','停水','奖学金','假期','放假','停 电','停 水'])
    print(content)



