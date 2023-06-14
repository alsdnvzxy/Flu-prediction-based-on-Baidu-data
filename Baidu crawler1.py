from datetime import date
from baidux.utils import test_cookies
from baidux import config
from baidux import BaiduIndex
from lxml import etree
import xlwt
book=xlwt.Workbook(encoding='utf-8')
cookies='BAIDUID=9DDD805B088EA81D659FD415DEFF855D:FG=1; BIDUPSID=9DDD805B088EA81D8B41D35C9C2F7E4D; PSTM=1627552858; BDUSS=1UwT0tPbFpnOTdYV2h3TVBIbHpuOHgzRTB-M2FjWnJBN0U5M0JTanRKVnBmMzlpRVFBQUFBJCQAAAAAAAAAAAEAAAB4Vo1h38vfy9~LamluZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGnyV2Jp8ldiZ; __yjs_duid=1_bec0dbe8ceef5a2d4dacc41c835a1c3b1628595412860; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1648976764,1649581506,1649682235,1651568116; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%221636652664%22%2C%22scope%22%3A1%7D%7D; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=8gagal81848l8hak4r1h6vco10q; BDRCVFR[Fc9oatPmwxn]=srT4swvGNE6uzdhUL68mv3; delPer=0; PSINO=5; H_PS_PSSID=36309_31660_36004_36166_34584_35978_36340_35802_36233_26350_36312_36061; BCLID=7820021138827263339; BDSFRCVID=IqtOJexroG0leprDtyEUb7uLicpWxY5TDYrELPfiaimDVu-VJeC6EG0Pts1-dEu-EHtdogKKyeOTHuCF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbCeoK0-tDt3qn7I5-joKRtQbfobejLDMI5KXJjVHJO_bpvTQxnkbftDyb5IJRciJmnJ-hnNKD3h8bTTyU42bU47yMvQ2q5W56RPanrEan_2SlcNLTjpQT8r5MDOK5OibCrt-nvLab3vOIJTXpO1jxPzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-Ftqj_s2Cob04P8KJjEe-Kk-PnVeUFL5-nZKRvHa2kjWn5M-qbMJq5a-6JhX-FSKbJOX6Qn3N5HKlRx5JTHjJ6e3R_V3xI8LNj405OTbTADsRbNb66pO-bghPJvynF8XnO7-xJlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVJO-KKC5hCIRDfK; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1651568136; RT="z=1&dm=baidu.com&si=8a7iwhio16v&ss=l2px0h00&sl=4&tt=3vz&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; ab_sr=1.0.1_MjUwZmY2MjVkODU5ODI3ZmZkM2NhMWY3MmMzN2E4Y2EyOTc3YmE1NGYzZTZmYWZkMDE4ZjBlZGFjZTVhY2IwYTU5OWM1YjE0NjQ5ZGJlZDE1MDU5MDQ3YjBkZDZjYTZhNDg5ZGIwMDBjZTEyZGJlNzExZTdlNWMwMGY2MjhmN2M5ZmFjNjg3MjJjMzg3ZDk3Y2JlYTJkNDA5YzY4NGYwMw==; __yjs_st=2_NGVhYjFlMGJiOWNhNzhhYjU4YzQwN2U4YzMzMGY4ZDBkMzk3MjQ2ODVmZjdmOWY4YjNhNWI4YjlkNDRlMzk4MmU4MzA4NWY4MmUyNWFjYmNkZjQ0OGVhY2FjM2EwODkwNGYxNWQ4MzM1MGYzYjY0MzExNWRlZjM4MGZiYjJiYTgyOTczNjZmZDczOGYzNDdmNjQ5YjkyNTg5NWZjZGIxNTY0NmFhMjc3YTcxYTgwYWU2YTkyODVkNjU0YzUwZjY3XzdfMzg5MWNhNGY=; bdindexid=1143ub4n6sbf9vmkbgqkbljes0'
print(test_cookies(cookies))
keywords=[['流感疫苗']]
#print(config.PROVINCE_CODE)
#print(config.CITY_CODE)
baidu_index = BaiduIndex(
    keywords=keywords,
    start_date='2022-01-03',
    end_date='2022-04-10',
    cookies=cookies,
    )
sheet=book.add_sheet(keywords[0][0],cell_overwrite_ok=True)
dates=[]
indexs=[]
for index in baidu_index.get_index():
    dates.append(index['date'])
    indexs.append(index['index'])
for i in range (0,len(dates)):
    sheet.write(i,0,dates[i])
    sheet.write(i,1,indexs[i])
book.save('流感疫苗2022.xls')
