"""Run only inside the held crd-emulador flock. Account is already signed in."""
import subprocess,time,sys,json
from pathlib import Path
p=Path(__file__).parent; label=sys.argv[1]
def a(*args,stdout=None):
 return subprocess.run(['adb','-s','emulator-5554',*args],stdin=subprocess.DEVNULL,stdout=stdout or subprocess.DEVNULL,check=True)
def tap(x,y):a('shell','input','tap',str(x),str(y));time.sleep(2)
def capture(step):
 with (p/f'{label}-{step}.png').open('wb') as f:a('exec-out','screencap','-p',stdout=f)
steps=[]
def mark(name):steps.append({'step':name,'epoch':time.time()})
a('shell','am','force-stop','com.conocerd.app'); a('logcat','-c')
a('shell','monkey','-p','com.conocerd.app','1');time.sleep(18)
mark('cold-start');capture('cold-start')
if label.startswith('guide'):
 tap(350,313) # Collapse the new guide so the shared destination result is reachable.
# Profile via the common top-right Explore entry, avoiding varying dock widths.
tap(347,82);time.sleep(3);mark('profile');capture('profile')
a('shell','input','keyevent','4');time.sleep(2)
# Search and destination are shared by both commits.
tap(135,142);a('shell','input','text','Monumento');time.sleep(4)
mark('search');capture('search')
tap(111,377);time.sleep(4);mark('detail');capture('detail')
tap(34,79);time.sleep(2);tap(329,79);mark('return-explore');capture('returned')
with (p/f'{label}-private.log').open('wb') as f:a('logcat','-d',stdout=f)
(p/f'{label}-steps.json').write_text(json.dumps(steps,indent=2))
print(label,'flow finished; captures and log saved')
