# 봇 커스텀 커맨드 생성기


## 사용법

pip install Customcmd

```py
from Customcmd import Custom

client = Custom.client(name= "testbot")

Custom.new(client, command="안녕", reply="안녕하세요!", author="decave27")

cmd = input("명령어를 입력하세요:")

reply = Custom.read(client, command=cmd)

print(reply)
```



사용중에 오류가 있거나 버그를 발견하면 이슈에 

## Contact to Me!
- [Mail](mailto:decave27@gmail.com)
- [Github](https://github.com/decave27)

