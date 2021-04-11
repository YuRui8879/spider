# 北京工业大学内网通知爬虫

声明：本程序仅用于学习用途，请勿频繁向服务器发送请求

## 函数接口
* login(username,password)  #用于登录内网
* index_html(cookie)  #用于获取主页面
* notification_html(cookie,index) #用于获取通知页面
* get_wid_and_ref(strhtml) #用于获取通知连接
* wid_html(cookie,wid) #根据wid获取相应html
* href_html(href) #根据href获取相应html
* analysis_text(a) #分析html文本
* analysis_table(a) #分析html表格
* select_notification(dic,cookie,sels) #按关键字选择通知

## 用法
### login(username,password)
用途：用于登录内网

参数：username：登录用户名；password：登录密码

返回：cookie

说明：该cookie用于构造下一次请求的头部
### index_html(cookie)
用途：用于获取主页面

参数：cookie：由login返回的cookie

返回：cookie

说明：在请求主页面时，cookie会发生变化，返回cookie用于下一次请求。如果要实现其他功能，通过在该页面查找对应的标签以实现扩展

### notification_html(cookie,index)
用途：用于获取通知页面

参数：cookie：由index_html返回的cookie；index：页数

返回：cookie，html

说明：通知内容通过AJAX技术实现，直接搜索标签并不会得到相应的内容。该函数返回的html中包含了标题，wid，href，发布部门，发布时间等主要信息，通过解析该html，可以获得相应的连接及标题等内容
### get_wid_and_ref(strhtml)
用途：用于获取通知连接

参数：strhtml：由notification_html返回的html

返回：res

说明：该函数用于解析notification_html获取的html，返回的res是一个列表，每一项是1个通知，通知用一个字典包含。字典的结构为
```
item = {'title': '', 'time': '', 'publis_dept': '', 'wid': '', 'href': ''}
```
部分通知使用wid作为索引，而部分通知使用href作为索引

### wid_html(cookie,wid)

用途：根据wid获取相应html

参数：cookie：由notification_ html返回的cookie；wid：由get_wid_and_ref返回的wid

返回：content

说明：该函数的返回值就是通知的内容

### href_html(href)

用途：根据href获取相应html

参数：href：由get_wid_and_ref返回的href

返回：content

说明：该函数的返回值就是通知的内容

### analysis_text(a)

用途：分析文本

参数：a：html的p节点

返回：txt

说明：返回分析后的文本内容

### analysis_table(a)

用途：分析表格

参数：a：html的tbody的children，是一个迭代对象

返回：txt

说明：返回分析后的文本内容

### select_notification(dic,cookie,sels)

用途：按关键字选择通知

参数：dic:由get_wid_and_ref(strhtml)返回的字典列表；cookie：由notification_html返回的cookie；sels：需要进行筛选的关键字

返回：content

说明：返回筛选之后的通知内容
