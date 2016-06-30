#update_maven_version
##批量升级maven中的第三方库版本
项目原始地址：https://github.com/Elin-Zhou/update_maven_version

在公司内部开发时，如果开发的项目非常多，而且引用用到了他人的项目，而他人的项目进行了重要升级导致必须全面升级时，逐个项目修改pom文件非常麻烦，遂可用本工具进行批量替换

注意，目前只考虑artifactId唯一的情况

使用python版本3.4

使用方法：

	py update_maven_version.py
    
    
