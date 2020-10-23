#Custom-Cmd


#봇 생성(Client)

```py
Custom.client(name="봇 이름")
```
#명령어 생성(new)

```py
Custom.new(client=[봇 클라이언트(class)], command=[사용자가 물어볼 명령어(str)], reply=[봇이 대답할 명령어(str)], author=[명령어를 만든 사람(class, str)], blacklist=[명령어로 사용할 단어 중에 검사(str)])
#blacklist에 걸리면 "blacklist" 반환

```
#명령어 삭제(remove)

```py
Custom.remove(client=[봇 클라이언트(class)], command=[사용자가 물어볼 명령어[이미 설정된 명령어](str)])
```

#명령어 읽기(read)

```py
Custom.read(client=[봇 클라이언트(class)], command=[사용자가 물어볼 명령어[이미 설정된 명령어](str)])
#reply로 설정된 값을 (str)로 반환
```
#명령어 정보(getinfo)

```py
Custom.getinfo(client=[봇 클라이언트(class)], command=[사용자가 물어볼 명령어[이미 설정된 명령어](str)])
#reply로 설정된 값을 (str)로 반환, 명령어 만든 시간을 (str)로 반환, author를 입력한 형식으로 반환
```

#명령어 정보 읽기(readinfo)

```py
Custom.readinfo(client=[봇 클라이언트(class)], command=[사용자가 물어볼 명령어[이미 설정된 명령어](str)])
#reply로 설정된 값을 (str)로 반환, author를 입력한 형식으로 반환
```

#봇 클라이언트 정보(clientinfo)

```py
Custom.clientinfo(client=[봇 클라이언트(class)])
#명령어 갯수를 (int) 로 반환, 봇 이름(클라이언트 이름)을 (str)로 반환
```

#Json 형식으로 명령어 정보 읽기(readjson)

```py
Custom.readjson(client=[봇 클라이언트(class)], command=[사용자가 물어볼 명령어[이미 설정된 명령어](str)])
#다음과 같이 json 형식으로 반환 : [명령어 이름(str)]: {'reply': (str), 'timestamp': (str), 'author': ()}
```

#에러 반환

모든 명령어는 명령어를 찾을 수 없으면

Command not found를 반환한다










## Contact to Me!
- [Mail](mailto:decave27@gmail.com)
- [Github](https://github.com/decave27)

