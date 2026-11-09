"""Builds index.html: the listening app, one self-contained file (three.js, data and ground image inside).
Recordings: put files in sounds/ and list them in sounds.json as
[{"src":"sounds/data4_fence_night.m4a","label":"DATA4 Jawczyce, fence, night","place":"Przyparkowa","date":"2026-11-13","dB":52}]"""
import json, os
here=os.path.dirname(os.path.abspath(__file__))
D=json.load(open(os.path.join(here,'../site/data2.json'))); M=json.load(open(os.path.join(here,'../site/media2.json')))
keep=['DISC','B','H','NL','pe','po','HAT','SUB','TW','lines','IMB']
d={k:D[k] for k in keep}; d['NL']={'n40':D['NL']['n40']}
d['lines']={k:D['lines'][k] for k in ('a','b','pw220','pw110')}
recs=json.load(open(os.path.join(here,'sounds.json'))) if os.path.exists(os.path.join(here,'sounds.json')) else []
t=open(os.path.join(here,'tpl.html')).read()
t=t.replace('/*THREE*/',open(os.path.join(here,'three_pkg/package/build/three.min.js')).read())
t=t.replace('const D=/*DATA*/null;','const D='+json.dumps(d,separators=(',',':'))+';')
t=t.replace('const BASE=/*BASE*/null;','const BASE='+json.dumps(M['BASE'])+';')
t=t.replace('const RECS=/*RECS*/[];','const RECS='+json.dumps(recs)+';')
os.makedirs(os.path.join(here,'out'),exist_ok=True)
open(os.path.join(here,'out/index.html'),'w').write(t); print('index.html',round(len(t)/1e6,2),'MB, recordings',len(recs))
