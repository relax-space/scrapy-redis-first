# scrapy_redis_second

## 步骤

### 创建项目
``` bash
scrapy startproject scrapy_redis_second

cd scrapy_redis_second
scrapy genspider gitee_project https://gitee.com

```

### 编写代码内容
- spiders/gitee_project.py
- pipelines.py
- settings.py

### 运行
```
# 在scrapy.cfg的同级目录下, 执行下面语句
scrapy runspider scrapy_redis_second/spiders/gitee_project.py
```