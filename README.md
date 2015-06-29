# 雨否 yufou

今天你的城市下雨吗？

[![Build Status](https://travis-ci.org/bcho/yufou.svg)](https://travis-ci.org/bcho/yufou)


##  使用示例 Usage

### 获取一张雷达图片

```python
>>> import yufou
>>> yufou.radar.radar_station_from_city(' 广州')
{'latitude': 23.1317346641, 'radar': 'AZ9200', 'city': '广州', 'longitude': 113.2590285241}
>>> yufou.radar.image('AZ9200')
http://image.nmc.cn/product/2015/201506/20150629/RDCP/medium/SEVP_AOC_RDCP_SLDAS_EBREF_AZ9200_L88_PI_20150629075000000.GIF
```



## TODO

- [ ] 通过地名反查附近雷达 (geo?)


## LICENSE

MIT
