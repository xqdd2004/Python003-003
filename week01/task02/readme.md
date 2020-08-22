作业二：

使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

猫眼电影网址： https://maoyan.com/films?showType=3

要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。



实现思路:

1、和作业1思路基本一致

2、在https://maoyan.com/films?showType=3这个页面获取电影信息，没有到详情页中去获取

3、到电影详情页获取电影信息，作为练手使用

4、Cookie是使用在setting.py文件修改的方式，后续计划实现cookies池和添加代理池的方式

​      目前访问猫眼的cookie的时效性差，很快就被反爬了

