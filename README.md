PROJECT TCP CHATROOM PYTHON

==================================================
TUJUAN PROJECT
==============

Membuat aplikasi chatroom sederhana menggunakan
protokol TCP dengan bahasa Python.

Topologi:

* 1 Server
* Beberapa Client
* Semua komunikasi melalui server

==================================================
KONSEP DASAR
============

TCP (Transmission Control Protocol):

* Connection-oriented
* Reliable
* Data pasti sampai
* Digunakan untuk chat, web, login, dll

Client:

* Menghubungkan diri ke server
* Mengirim pesan
* Menerima broadcast pesan

Server:

* Menunggu koneksi client
* Menyimpan daftar client
* Meneruskan pesan ke client lain

==================================================
FILE PROJECT
============

tcp-chat/
│
├── server.py
└── client.py

==================================================
LIBRARY YANG DIGUNAKAN
======================

import socket
import threading

socket:
Untuk komunikasi jaringan TCP

threading:
Agar bisa handle banyak client sekaligus

==================================================
LANGKAH MENJALANKAN
===================

1. Jalankan server

python server.py

2. Jalankan client

python client.py

3. Masukkan IP server

Jika masih 1 laptop:
127.0.0.1

Jika beda laptop:
gunakan IP laptop server
contoh:
192.168.1.5

==================================================
ALUR PROGRAM
============

1. Server aktif dan listen pada port 9999

2. Client connect ke server

3. Server menerima client baru

4. Client mengirim pesan

5. Server menerima pesan

6. Server broadcast ke semua client lain

==================================================
PENJELASAN PENTING
==================

IP Address:
Alamat device pada jaringan

Port:
Alamat aplikasi pada device

Contoh:
192.168.1.5:9999

192.168.1.5  = device
9999         = aplikasi chat

==================================================
THREADING
=========

Digunakan agar:

* Banyak client bisa aktif bersamaan
* Server tidak hanya melayani 1 client

Setiap client memiliki thread sendiri.

==================================================
PERBEDAAN TCP DAN UDP
=====================

TCP:

* Reliable
* Ada koneksi
* Data pasti sampai
* Cocok untuk chat

UDP:

* Lebih cepat
* Tidak reliable
* Tidak ada koneksi
* Cocok untuk game/streaming

==================================================
HASIL AKHIR
===========

Contoh output: (pada server)

=== Client 1 joined the chat ===

[Client 1] halo semua
[Client 2] hai juga

==================================================
KESIMPULAN
==========

Project ini merupakan implementasi dasar
socket programming menggunakan protokol TCP
dengan konsep client-server dan broadcast message.
