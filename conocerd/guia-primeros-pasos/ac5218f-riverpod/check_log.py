import json,re,sys
from pathlib import Path
p=Path(sys.argv[1]); lines=p.read_text().splitlines()
events=[]
for i,line in enumerate(lines):
 if 'setState() or markNeedsBuild() called during build.' in line and '\x1b' not in line:
  widget='unknown'
  for n in range(i,min(i+12,len(lines)-1)):
   if 'currently being built' in lines[n]:widget=lines[n+1].split('I flutter :',1)[-1].strip();break
  events.append({'time':line[:18],'widget':widget})
print(json.dumps({'log':p.name,'errorCount':len(events),'events':events},indent=2))
sys.exit(bool(events))
