[![Build Status](https://travis-ci.org/guangrei/pytanggalmerah.svg?branch=master)](https://travis-ci.org/guangrei/pytanggalmerah)

**Pytanggalmerah** adalah module python untuk mengecek tanggal merah berdasarkan hari minggu dan hari libur nasional.

### installasi

```
pip install pytanggalmerah
```

### menggunakan Pytanggalmerah

``` python
from pytanggalmerah import TanggalMerah

t = TanggalMerah()
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
 **menggunakan module offline**

untuk memastikan data slalu update module ini mengharuskan terhubung ke internet, namun opsi untuk menggunakan offline juga tersedia.

pastikan sudah mendownload [calendar.json](https://github.com/guangrei/Json-Indonesia-holidays/raw/master/calendar.json)


```python
t = TanggalMerah("lokasi/calendar.json")

```
### sumber data

**pytanggalmerah** menggunakan data yang bersumber dari google calendar, data yang telah lampau mungkin tidak tersedia & data yang sekarang masih bisa direvisi.