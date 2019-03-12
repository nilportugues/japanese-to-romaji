# japanese-to-romaji

- run `install.sh` (will install Python3)
- run `python3 api/app.py`

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

```json
{
    "data": "ここに蔓延る摩天楼\n君の確かな芽を摘んできた\n\n叶えたいもの全て奪い攫っては\n僕をねじ曲げてく\n\n価値観違い\n嫌いなあいつは\n滑稽なんて嗤いあって\n上品な言葉\n乗せあって待って焦って足掻いた\nせっせ\n知恵を絞って\nせっせ\n欲をかいて\nエゴに堕ちてゆけ\n\nあなたは言った\n消耗品さ\nだけど私は\nまだ考えてるわ\nいつかまた\nこうやって\n踊ってやってくれないか\n\n辛気を纏った\n少年少女\n憂さを晴らした\nイエスマン患者\n誰も何者でもないもの\n真意を知れば最期になるならさ\n舌が乾くまで話そうぜ\n\n虚勢を張って\n自分を失った\n虚言を吐いて\n幻になった\n\n馬鹿になって\n宙を舞って\nしたらもう\n壊れてしまいました\n\n純粋で透明な少年のさ\n感情に魔を差してやってんのさ\n\n思い出して思い出して考えては\n辿り着きさえもしないや\n\nあなたが言った\n本当の意を\n世界の片隅で考えてるわ\n\n冷えきった\n嘘さえも\n溶かしてやってくれるのなら\n\n孤独を知った才能人と\n明日を選んだ\nメランコリー患者\n\n戻れない僕にさようなら\n指を加えて\n泣いても無駄だから\nいつかまた\n\n最終列車を待つわ\nあなたの帰りはないけど\nここに居るべきではないこと\n今全てを飲みこめやしないけど\n\n遠くからみたら\nあなた幸せそうねでも\n痛くて\n痛くて\n全部知ってるから\n\nあなたは言った\n消耗品さ\nだけど私は\nまだ考えてるわ\nいつかまた\nこうやって\n踊ってやってくれないか\n\n辛気を纏った\n少年少女\n憂さを晴らした\nイエスマン患者\n誰も何者でもないもの\n真意を知れば最期になるならさ\n舌が乾くまで話そうぜ\n\nそして僕ら逸話になって\n今不確かな笑みを浮かべては\n誰も知らなかった物語を今\n君に話すから"
}

```
