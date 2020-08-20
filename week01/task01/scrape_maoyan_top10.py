#作业一：
#
#安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


#user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
#临时代理，运行时需要随时替换
proxies = { "http": "http://116.62.150.144:25939", "https": "http://116.62.150.144:25939"} 
cookies = '__mta=156120324.1597742408223.1597751543169.1597830931897.7; uuid_n_v=v1; uuid=01A263B0E13411EAABD8ED85325F9646EA385D5F6E304B69AC27F29C8E27F9C6; _lxsdk_cuid=17400de61c5c8-03530536a5e45c-31657304-1aeaa0-17400de61c5c8; _lxsdk=01A263B0E13411EAABD8ED85325F9646EA385D5F6E304B69AC27F29C8E27F9C6; mojo-uuid=a95cb5455a48d6d591cb8bcb70793d6b; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597742408,1597747376,1597814426; mojo-session-id={"id":"0cdec406216dd41be5e4e0091f69aff7","time":1597936766746}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597937862; _lxsdk_s=1740c740fb2-258-bce-5a7%7C%7C3; __mta=156120324.1597742408223.1597830931897.1597937862135.8'
#获取网页内容，使用requests获取猫眼电影页
def get_html(url):
    headers={'User-Agent': user_agent, "Cookie": cookies}
    res = requests.get(url, headers=headers)
    if(res.status_code == requests.codes.ok):
        content = res.text
        return res.text
    return

#用BeautifulSoup解析网页内容，提取所需的电影名称、电影类型和上映时间
def parse_html_bs4( content ):
    soup = BeautifulSoup(content,'html.parser')
    list = []
    for tags in soup.findAll('div', attrs={'class':'movie-item-hover'}):
        #电影名称、电影类型和上映时间
        for atag in tags.find_all('div', attrs={'class':'movie-hover-title'}):
            childTag1 = atag.contents[1]
            class_name = childTag1.attrs['class'][0]      
            if class_name=='name' :
                movie_name = childTag1.contents[0]
                continue
            if class_name =='hover-tag': 
                tag_content = childTag1.contents[0]
            if tag_content =='类型:':
                movie_type = atag.contents[2].replace('\\n','').strip()
                continue
            if tag_content =='主演:':
                movie_actors = atag.contents[2].replace('\\n','').strip()
                continue
            if tag_content =='上映时间:':
                movie_release_time = atag.contents[2].replace('\\n','').strip()
                continue           
        movie_info = [movie_name, movie_type, movie_actors, movie_release_time]
        list.append(movie_info)
   
    return list

#从文件中读取数据，用来测试电影信息提取
def read_data ( filename ):
    with open(filename,'r') as f:  
        content = f.read();  
        return content
    return

#保存数据到文件中
def save_data_file( filename, data ):
    if (os.path.exists(filename)):
        file = open(filename, "a", encoding='utf-8')       
        file.write(data)
        file.close()
    else:
        file = open(filename, "w", encoding='utf-8')
        file.write(data)
        file.close()
    return


#保存数据到CVS文件中
def save_data_csv(filename, data, size):
    df = pd.DataFrame( data[:size] )
    if (os.path.exists(filename)):
        file = open(filename, "a", encoding='utf-8')
        df.to_csv(file, header=False, line_terminator="\n", index=False)
        file.close()
    else:
        file = open(filename, "w", encoding='utf-8')
        df.to_csv(file, header=False,line_terminator="\n", index=False)
        file.close()
    return

if __name__ == "__main__":
    start_url = 'https://maoyan.com/films?showType=3'
    content = get_html(start_url)
    #自己开发测试所用
    #filename1 = "maoyan_movie.txt"
    filename = "maoyan_moive_top10.csv"
    #保存页面html到本地文件
    #save_data_file(filename, content)
    #测试时所用，从文件中读取网页内容
    #content = read_data(filename1)

    data_list = parse_html_bs4( content )
    save_data_csv(filename, data_list, 10)
