### Derste konuşulduğunun aksine vize ve final olacaktır. Nisan 2. Hafta Vize.
korkulacak bir şey yok ödevlerinizi yaptığınız sürece (Elimden olmayan nedenlerden ötürü)

Final sınavında week7 altındaki sorulardan sorumlusunuz. Ayrıca

1. Internet üstünde bir sayfaya istekte buludun. Hangi libraryleri kullanırsın </p>
2. strace ne işe yarar</p>
3. DOM Tree nedir ?</p>
4. sql injectionsız hale getir </p>

```python3

import sqlite3
conn = sqlite3.connect('hackers.db')

username = input("username: ")
c = conn.cursor()
c.execute("SELECT count(*) FROM users "
"WHERE username = '%s'"%username)

print (c.fetchone())

```


5. Thread nedir nasıl kullanılır ? </p>
6. ThreadPool nedir </p>
7. XML Web Service ile Rest servisin farkı nedir ? </p>
8. Rest servisi, XML Webservice göre tercih etmenizin nedeni nedir ?  </p>
9. Rest servis yazacaksanız pythonun hangi modülünü kullanırsınız ? </p>
10. </p>
```python3
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
```
</p>
class HelloWorld(Resource): yazdığımızda içine hangi GET / PUT  isteklerini karşılamak istersek hangi methodları yazmamız gerekiyor</p>



11. http://api.bilgi.edu.tr/hello servisinden çıktısı verilen bir servis mevcuttur.</p>

```json
{
    "data": "Final var"
}
```
bu servisin ekrana Final var yazdıracak şekilde client kodunu yazınız..
```python3
from urllib import request
import json

req = request.urlopen("http://localhost:5000")
data =  req.read()
jData = json.loads(str(data,"UTF-8"))
print(jData["data"])
```
