import json, math

def num(x): return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)
def pos(x): return num(x) and x>0
def jround(x): return math.floor(x+0.5)
def r1(x): return jround(x*10)/10
def r2(x): return jround(x*100)/100
def jsnum(x):
    if isinstance(x,float) and x==int(x): return str(int(x))
    return str(x)

LOAD=1.4; EFF=0.8; VOLTS=120; W_PER_HP=746

def tonnage_plan(diameter,factor,rating):
    if not pos(diameter): return {"error":"the round diameter must be above zero"}
    if not pos(factor): return {"error":"the wood factor must be above zero"}
    if not pos(rating): return {"error":"the box tonnage must be above zero"}
    needed=diameter*factor
    margin=rating/needed*100
    if margin>=100: verdict="the ram covers the round"
    elif margin>=80: verdict="the ram stalls on the tough ones"
    else: verdict="the ram is outclassed"
    return {"needed":r1(needed),"margin":r1(margin),"verdict":verdict}

def render_tonnage(r,diameter,factor,rating):
    word=" ton an inch" if factor==1 else " tons an inch"
    return ("At "+jsnum(diameter)+" inches and "+jsnum(factor)+word+", the round wants "+jsnum(r["needed"])
            +" honest tons; the "+jsnum(rating)+"-ton box sits at "+jsnum(r["margin"])+"% of that, and "+r["verdict"]+".")

def cycle_plan(sticker):
    if not pos(sticker): return {"error":"the sticker cycle must be above zero"}
    honest=sticker*LOAD
    return {"honest":r1(honest),"perHour":r1(3600/honest)}

def render_cycle(r,sticker):
    return ("The "+jsnum(sticker)+"-second cycle on the sticker is the empty ram; under load the honest cycle is about "
            +jsnum(r["honest"])+" seconds, a pace of about "+jsnum(r["perHour"])+" rounds an hour.")

def circuit_plan(amps,claimed_hp):
    if not pos(amps): return {"error":"the circuit amps must be above zero"}
    if not pos(claimed_hp): return {"error":"the claimed horsepower must be above zero"}
    honest=VOLTS*amps*EFF/W_PER_HP
    ratio=claimed_hp/honest
    if ratio<=1: verdict="the sticker fits the circuit"
    elif ratio<=2: verdict="the sticker counts the startup surge"
    else: verdict="the sticker is marketing first"
    return {"honest":r2(honest),"ratio":r2(ratio),"verdict":verdict}

def render_circuit(r,amps,claimed_hp):
    return ("The "+jsnum(amps)+"-amp circuit honestly feeds about "+jsnum(r["honest"])
            +" horsepower after the continuous-load derate; the "+jsnum(claimed_hp)+"-horsepower sticker claims "
            +jsnum(r["ratio"])+" times that, and "+r["verdict"]+".")

cases=[]
def add(tool,args):
    if tool=="tonnage": r=tonnage_plan(*args); fn=render_tonnage
    elif tool=="cycle": r=cycle_plan(*args); fn=render_cycle
    else: r=circuit_plan(*args); fn=render_circuit
    case={"tool":tool,"args":args,"result":r}
    if "error" not in r: case["render"]=fn(r,*args)
    cases.append(case)

for a in [(16,1,22),(12,0.5,7),(20,1.5,25),(18,1,22),(24,1.5,34),(10,0.75,6)]:
    add("tonnage",a)
for a in [(13,),(10,),(15,),(18,),(25,),(11,)]:
    add("cycle",a)
for a in [(15,2),(15,1.5),(20,3),(15,2.5),(15,5),(20,2)]:
    add("circuit",a)
add("tonnage",[0,1,22]); add("tonnage",[16,0,22]); add("tonnage",[16,1,0])
add("cycle",[0]); add("cycle",["fast"])
add("circuit",[0,2]); add("circuit",[15,0]); add("circuit",[15,"big"])

json.dump(cases,open("expected.json","w"),separators=(",",":"))
print(len(cases),"cases")
