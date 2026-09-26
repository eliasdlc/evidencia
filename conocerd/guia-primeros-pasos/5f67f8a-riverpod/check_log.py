import json,re,sys
from pathlib import Path
p=Path(sys.argv[1]); text=p.read_text(errors="replace")
text=re.sub(r"\x1b\[[0-9;]*m", "", text)
patterns={
 "buildPhase":r"setState\(\) or markNeedsBuild\(\) called during build",
 "providerModifiedDuringBuild":r"Tried to modify a provider while the widget tree was building",
 "flutterException":r"EXCEPTION CAUGHT BY",
 "uncaughtZone":r"Uncaught zone error",
 "androidFatal":r"FATAL EXCEPTION",
 "overflow":r"A RenderFlex overflowed",
 "missingPlugin":r"MissingPluginException",
}
counts={name:len(re.findall(pattern,text)) for name,pattern in patterns.items()}
print(json.dumps({"log":p.name,"counts":counts},indent=2))
sys.exit(bool(counts["buildPhase"] or counts["providerModifiedDuringBuild"]))
