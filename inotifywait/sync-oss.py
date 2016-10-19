#!/bin/python
# -*- coding: utf-8 -*-

import inotify.adapters
import oss2
import os
import datetime

from oss2 import SizedFileAdapter, determine_part_size
from oss2.models import PartInfo

#上传阿里云（断点续传）
def _upload(fileName, remoteName):

	auth = oss2.Auth('您的AccessKeyId', '您的AccessKeySecret')
    bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', '您的bucket名')

    oss2.resumable_upload(bucket, remoteName, fileName,
        store=oss2.ResumableStore(root='/tmp'),
        multipart_threshold=10*1024*1024,
        part_size=10*1024*1024,
        num_threads=1)

def _main():

    #监控目录的路径
    path = '/usr/local/nginx/html/uploads'
    i = inotify.adapters.InotifyTree(path)

    file_path = "/usr/local/nginx/html/sync.log"

    try:
        for event in i.event_gen():
            if event is not None:

			    #监控事件
                (header, type_names, watch_path, filename) = event

                now = datetime.datetime.now()
                fileSrc = watch_path+'/'+filename
                if watch_path == path:
                    remoteName = filename
                else:
                    remoteName = watch_path[33:]+'/'+filename
 
                f = open(file_path, "a")
				
				#判断有新增的后缀名为.zip或.mp4的文件，将断点上传到阿里云上
                if type_names == ['IN_CLOSE_WRITE'] and  os.path.splitext(fileSrc)[1] in ('.zip', '.mp4'):
                    f.write(now.strftime('%Y-%m-%d %H:%M:%S')+'    '+remoteName+'\n')
                    _upload(fileSrc, remoteName)
                f.close()
    finally:
        if (f):
            f.close()

if __name__ == '__main__':
    _main()

