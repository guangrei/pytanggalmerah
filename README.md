[![status workflow test](https://github.com/guangrei/pytanggalmerah/actions/workflows/python-app.yml/badge.svg)](https://github.com/guangrei/pytanggalmerah/actions) [![status workflow build](https://github.com/guangrei/pytanggalmerah/actions/workflows/release_to_pypi.yml/badge.svg)](https://github.com/guangrei/pytanggalmerah/actions)


[![Downloads](https://static.pepy.tech/badge/pytanggalmerah)](https://pepy.tech/project/pytanggalmerah) [![Downloads](https://static.pepy.tech/badge/pytanggalmerah/month)](https://pepy.tech/project/pytanggalmerah) [![Downloads](https://static.pepy.tech/badge/pytanggalmerah/week)](https://pepy.tech/project/pytanggalmerah)

**Pytanggalmerah** adalah module python untuk mengecek tanggal merah berdasarkan hari minggu dan hari libur nasional.

### installasi

```
pip install pytanggalmerah
```

### menggunakan Pytanggalmerah

``` python
from pytanggalmerah import TanggalMerah

t = TanggalMerah(cache_path = None, cache_time = 600) # cache_path = None berarti directory cache automatis
t.check() # mengecek apakah tanggal merah, return boolean.
t.is_holiday() # mengecek apakah hari libur nasional, return  boolean.
t.is_sunday() # mengecek apakah hari minggu, return booelan.
t.get_event() # mendapatkan event, return list.

```
 **mengecek specific tanggal tertentu** 

``` python
t.set_date("2019", "02", "05")
t.check()
```
 **mengatur zona waktu** 

secara default zona waktu pytanggalmerah adalah Asia/Jakarta tapi bisa diubah, seperti

``` python
t.set_timezone("Asia/Makassar")
t.check()
```
 **menggunakan lewat terminal**


```
$ harilibur # check harilibur
$ harilibur 2022 04 15 # check harilibur dengan spesifikasi
$ TIMEZSET = "Asia/Makasar" harilibur # mengecek harilibur dengan spesifikasi timezone

```

> harilibur command hanya mengecek tanggal merah dan tidak termasuk hari minggu.
### sumber data

**pytanggalmerah** menggunakan data yang bersumber dari google calendar, data yang telah lampau mungkin tidak tersedia & data yang sekarang masih bisa direvisi.
