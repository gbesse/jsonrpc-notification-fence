import json,math
from .common import number,integer,identifier,unique_ids
import subprocess,sys
PEER="""import json,sys
for line in sys.stdin:
 m=json.loads(line)
 if 'id' not in m:continue
 if m.get('method')=='echo':reply={'jsonrpc':'2.0','id':m['id'],'result':m.get('params')}
 else:reply={'jsonrpc':'2.0','id':m['id'],'error':{'code':-32601,'message':'Method not found'}}
 print(json.dumps(reply),flush=True)
"""
def run(d):
 messages=d['messages']
 if not isinstance(messages,list)or len(messages)>1000:raise ValueError('messages')
 for m in messages:
  if m.get('jsonrpc')!='2.0' or not isinstance(m.get('method'),str):raise ValueError('request')
  if 'id'in m and m['id']is not None and type(m['id'])not in [str,int]:raise ValueError('id')
 raw=''.join(json.dumps(m,allow_nan=False)+'\n'for m in messages)
 if len(raw)>100000:raise ValueError('size')
 process=subprocess.run([sys.executable,'-I','-c',PEER],input=raw,capture_output=True,text=True,timeout=5,check=True);replies=[json.loads(line)for line in process.stdout.splitlines()];ids=[(type(m['id']).__name__,m['id'])for m in messages if'id'in m]
 return dict(replies=replies,requests=len(ids),notifications=len(messages)-len(ids),typed_id_collisions=len(ids)-len(set(ids)),null_ids=sum(m.get('id','absent')is None for m in messages),naive_expected_replies=len(messages),actual_expected_replies=len(ids))
