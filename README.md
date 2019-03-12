# japanese-to-romaji

- run `install.sh` (will install Python3)
- run `python3 example.py`

## To do


- Dockerize and use an `python:3.7.2-slim-stretch`
- Build an API or Queue system to receive kanji text and return romaji

## For project

- Scrap http://j-lyric.net/artist/a0592ff/l04aa2b.html :)
- Build a queue to provide translations in english of every song.



## 2.1 Documentation: 

 - **Swagger UI**: http://127.0.0.1:5000/
 - **Swagger.json**: http://127.0.0.1:5000/swagger.json
 
# 3. Framework:

API has been written in Python 3 and uses the Flask-RESTful framework.
 
# 4. Example

```sh
curl -X POST \
  http://nilportugues.com:5000/to-romaji \
  -H 'Authorization: key=BJFfIhYJIx1qtxNbwycJl7RMks_lf1oB38U7u5d70LWdQ0aZHj75RGy_BCwg-ADPPaQoFFsKmadoDiIf-ATQPac' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: c16faad6-23e5-4c89-98b7-ecb4670b128e' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F 'data=ずっと前から言っていた
あーだのこーだの愛されたい
ずっと前から言っていた
安心探して粗探し
ずっと前から知っていた
好きと嫌いの取っ組み合い
「ずっと前から知っていた。」
みたいだって話したあの日
純情
論争
あなたのそういうところが嫌いです
嫌いです
でも嫌いになれない
どうして
純情
論争
あなたのそういうところが嫌いです
やかましいし騒がしいし
好きも嫌いもあなた次第
ずっと前から知っていた
いやよいやよも好きのうち
ずっと前から知っていた
狂ったふりしてすっからかん
ずっと前から知っていた
狐につままれたら気付けって
嘘の自分で好かれるよりもホントの自分で嫌われよう
純情
論争
あなたのそういうところが嫌いです
嫌いです
でも嫌いになれない
どうして
純情
論争
あなたのそういうところが嫌いです
嫌いです
でも素直になれない嫌い嫌いと言ってないで
だってだって大大嫌いになってもまた思い出して
相思相愛そうそうにない想像して溺れちゃって
だから
純情
論争
あなたのそういうところが嫌いです
やかましいし騒がしいけど
だけどそんなに嫌いじゃない
純情
論争
あなたのそういうところが嫌いです
嫌いです
でも嫌いになれないどうして
純情
論争
あなたのそういうところが嫌いです
嫌いです
でも素直になれない嫌い嫌いと言ってないで
だってだって毎回期待を裂いてはまたなぞっちゃって
好機到来
構想未来
行動して求めちゃって
だから
純情
論争
あなたのそういうところが嫌いです
狂おしいほど悩ましいけど
だけどそんなに嫌いじゃない
狂おしいほど噛みしめたい'


```
