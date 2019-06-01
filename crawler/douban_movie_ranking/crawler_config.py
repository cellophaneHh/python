# 豆瓣电影详情页配置
movieInfoConfig = {
    "name":
    "//div[@id='content']/h1/span[1]/text()",
    "year":
    "//div[@id='content']/h1/span[2]/text()",
    "playBill":
    "//div[@id='content']//div[@id='mainpic']/a/img/@src",
    "directors":
    "//div[@id='content']//div[@id='info']/span[1]/span[2]/a/text()",
    "scriptWriters":
    "//div[@id='content']//div[@id='info']/span[2]/span[2]/a/text()",
    "mainActors":
    "//div[@id='content']//div[@id='info']/span[@class='actor']/span[@class='attrs']/a/text()",
    "types":
    "//div[@id='content']//div[@id='info']/span[@property='v:genre']/text()",
    "site":
    "//div[@id='content']//div[@id='info']/span[text() = '官方网站:']/following::a[1]/@href",
    "region":
    "normalize-space(//div[@id='content']//div[@id='info']/span[text() = '制片国家/地区:']/following::text()[1])",
    "language":
    "normalize-space(//div[@id='content']//div[@id='info']/span[text() = '语言:']/following::text()[1])",
    "releaseDate":
    "//div[@id='content']//div[@id='info']/span[text() = '上映日期:']/following::span[1]/@content",
    "fileLength":
    "normalize-space(//div[@id='content']//div[@id='info']/span[text() = '片长:']/following::span[1]/@content)",
    "alternateName":
    "normalize-space(//div[@id='content']//div[@id='info']/span[text() = '又名:']/following::text()[1])",
    "imdbLink":
    "normalize-space(//div[@id='content']//div[@id='info']/span[text() = 'IMDb链接:']/following::a[1]/@href)"
}
