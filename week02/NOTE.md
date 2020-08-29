学习笔记

1、经过本周的教程学习，明白了如何查看浏览器头，并优化了上周的作业
2、重点学习了python如何操作mysql部分的内容，并找了一个操作mysql通用的工具方法类，对于理解python如何操作DB非常有帮助
3、用selenium模拟浏览器实现登录石墨的过程中
   3.1异常信息
   SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 85
   原因是驱动版本和本机浏览器版本不一致，替换和本机chrome浏览器版本一致后就正常
   3.2驱动路径
   驱动路径： /urs/local/bin
   3.3指定驱动路径 webDriver.chrome()