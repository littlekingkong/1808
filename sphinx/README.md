# sphinx

1、在官网下载：http://sphinxsearch.com/downloads/

2、根据文档安装：http://sphinxsearch.com/docs/current.html

3、copy一份sphinx-min.conf.dist，命名为sphinx.conf

4、配置sphinx.conf

参考文章：http://www.cnblogs.com/yjf512/p/3598332.html

5、添加系统任务

   a.每5分钟执行一次增量索引，并合并到全索引中
   
   /usr/local/sphinx/bin/indexer --config /usr/local/sphinx/etc/sphinx.conf idx_app_delta idx_video_delta --rotate &&  /usr/local/sphinx/bin/indexer --config /usr/local/sphinx/etc/sphinx.conf --merge idx_app idx_app_delta --rotate && /usr/local/sphinx/bin/indexer --config /usr/local/sphinx/etc/sphinx.conf --merge idx_video idx_video_delta --rotate
   
   b.每天凌晨执行一次全量索引
   
   /usr/local/sphinx/bin/indexer -c /usr/local/sphinx/etc/sphinx.conf --rotate --all >> /usr/local/sphinx/var/log/main.log
   
6、编写search.php文件
   
