
import json
import os
import datetime
import time
class Custom:
    def __init__():
        return
    def client(self, name):
        with open(f'{name}.json', 'r', encoding='UTF8') as f:
            data = json.load(f)
            return data, name
    def new(self, client, command, reply, author=None, blacklist=None):
        if not blacklist == None:
            if command in blacklist or reply in blacklist:
                return "blacklist"
        command = str(command)
        reply = str(reply)
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        st = str(st)
        client.data[command : {'reply': reply, 'author': author, 'timestamp': st}]
        def save(data):
            with open(f'{client.name}.json', 'w', encoding='utf-8') as t:
                json.dump(client.data, t, indent="\t", ensure_ascii=False)
    def remove(self, client, command):
        try:
            with open(f'{client.name}.json', 'r', encoding='UTF8') as f:
                data = json.load(f)
            data[command]
            del command
            return 'removesuccess'
        except:
            raise Exception('Command not found')
    def read(self, client, command):
        try:
            with open(f'{client.name}.json', 'r', encoding='UTF8') as f:
                data = json.load(f)
            reply = data[command]['reply']
            return reply
        except:
            pass
    def getinfo(self, client, command):
        try:
            with open(f'{client.name}.json', 'r', encoding='UTF8') as f:
                data = json.load(f)
            reply = data[command]['reply']
            timestamp = data[command]['timestamp']
            author = data[command]['author']
            return reply, timestamp, author
        except:
            raise Exception('Command not found')
    def readinfo(self , client, command):
        try:
            with open(f'{client.name}.json', 'r', encoding='UTF8') as f:
                data = json.load(f)
            reply = data[command]['reply']
            author = data[command]['author']
            return reply, author
        except:
            pass
    def clientinfo(self, client, command):
        try:
            with open(f'{client.name}.json', 'r', encoding='UTF8') as f:
                data = json.load(f)
            count = len(data)
            name = client.name
            return count, name
        except:
            raise Exception('Command not found')
    def readjson(self, client, command):
        try:
            with open(f'{client.name}.json', 'r', encoding='UTF8') as f:
                data = json.load(f)
            reply = data[command]['reply']
            timestamp = data[command]['timestamp']
            author = data[command]['author']
            return {command: {'reply': reply, 'timestamp': timestamp, 'author': author}}
        except:
            raise Exception('Command not found')


