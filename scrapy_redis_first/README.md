# scrapy_redis_frist

## 步骤

### 创建项目
``` bash
scrapy startproject scrapy_redis_first

cd scrapy_redis_first
scrapy genspider gitee_project https://gitee.com

```

### 编写代码内容
- spiders/gitee_project.py
- pipelines.py
- settings.py

### 运行
```
# 在scrapy.cfg的同级目录下, 执行下面语句
scrapy runspider scrapy_redis_first/spiders/gitee_project.py
```