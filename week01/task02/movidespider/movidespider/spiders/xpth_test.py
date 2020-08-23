from lxml import etree
from scrapy.selector import Selector

#用本地文件来测试猫眼页面的xpath表达式

#从文件中读取数据，用来测试电影信息提取
def read_data ( filename ):
    with open(filename,'r') as f:  
        content = f.read();  
        return content
    return

def parse_xpath_lxml( web_data ):

    html = etree.HTML(web_data)
    print(html)
    html_data = html.xpath('//div[@class="movie-hover-info"]/div/text()')
    for movie in html_data:
        print('===========================')
        #a = html_data.xpath('//div/text()')
        print(movie)
   # print(html_data)
    pass

def parse_xpath_scrapy( web_data ):
    #web_data = web_data.replace('\n','').replace(' ','')
    selector = Selector(text=web_data)
    movie_list = selector.xpath('//div[@class="movie-hover-info"]')
    for movie_info in movie_list:
        print('===================')
        attr_list = movie_info.xpath('./div')
        print(attr_list[0].xpath('./@title').extract_first().strip())
        print(attr_list[1].xpath('./text()').extract()[1].strip())
        print(attr_list[2].xpath('./text()').extract()[1].strip())
        print(attr_list[3].xpath('./text()').extract()[1].strip())
        #print(movie_info)
        #print(movie_info.xpath('./div/text()'))

#
def save_item_csv ():
    movie_name = '大鱼海棠'
    movie_type = 'type'
    movie_actors = 'chenchen'
    movie_release_time = '2020-12-13'
    movie_info = f'{movie_name}, {movie_type}, {movie_release_time}, {movie_actors}\r\n'

    with open("./maoyan_movie.csv",'a+', encoding='utf-8') as file :
        file.write(movie_info)
        file.close()


if __name__ == "__main__":

    #自己开发测试所用
    #filename = "maoyan_movie.txt"
    #保存页面html到本地文件
    #save_data_file(filename, content)
    #测试时所用，从文件中读取网页内容
    #web_data = read_data(filename)

    #parse_xpath_scrapy( web_data )    
    save_item_csv()