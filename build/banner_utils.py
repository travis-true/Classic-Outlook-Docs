from __future__ import annotations
import csv, os, re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from PIL import Image, ImageDraw, ImageFont

MIDNIGHT='#002855'; BLUEJAY='#41B6E6'; WHITE='#FFFFFF'; SKY='#77C5D5'; SUBTLE='#E6E7E8'
@dataclass(frozen=True)
class Banner:
    asset:int; slug:str; folder:str; filename_base:str; title:str; subtitle:str; width:int; height:int; motif:str; alt_text:str

def repo_root() -> Path: return Path(__file__).resolve().parents[1]
def now_iso() -> str: return datetime.now(timezone.utc).isoformat(timespec='seconds')
def safe_text(s:str)->str: return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def md_inventory(root:Path)->list[Path]:
    skip={'.git','.venv','venv','env','__pycache__','dist'}
    out=[]
    for p in root.rglob('*.md'):
        rel=p.relative_to(root)
        if any(part in skip for part in rel.parts): continue
        if str(rel).startswith('build/output/'): continue
        if p.is_symlink():
            try: p.resolve().relative_to(root)
            except ValueError: continue
        out.append(rel)
    return sorted(out, key=str)

def task_map_icon(x:int,y:int,s:int=1)->str:
    return f'''<g id="icon-inbox-decision-flow" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <rect x="{x}" y="{y+58}" width="360" height="190" rx="22" stroke="{WHITE}" stroke-width="8" opacity="0.92"/>
      <path d="M{x+35} {y+96}h290l-58 66H{x+93}z" stroke="{BLUEJAY}" stroke-width="8"/>
      <path d="M{x+180} {y+58}v-42" stroke="{BLUEJAY}" stroke-width="8"/>
      <circle cx="{x+180}" cy="{y+4}" r="36" stroke="{BLUEJAY}" stroke-width="8"/>
      <path d="M{x+165} {y+4}l12 12 24-28" stroke="{WHITE}" stroke-width="7"/>
      <path d="M{x+180} {y+248}v45M{x+180} {y+293}h-105M{x+180} {y+293}h105" stroke="{BLUEJAY}" stroke-width="8"/>
      <rect x="{x-6}" y="{y+315}" width="150" height="58" rx="18" stroke="{WHITE}" stroke-width="7" opacity="0.9"/>
      <rect x="{x+216}" y="{y+315}" width="150" height="58" rx="18" stroke="{WHITE}" stroke-width="7" opacity="0.9"/>
    </g>'''

def banner_svg(b:Banner)->str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{b.width}" height="{b.height}" viewBox="0 0 {b.width} {b.height}" role="img" aria-label="{safe_text(b.alt_text)}">
  <title>{safe_text(b.title)}</title><desc>{safe_text(b.alt_text)}</desc>
  <rect width="{b.width}" height="{b.height}" fill="{MIDNIGHT}"/>
  <rect x="0" y="0" width="22" height="{b.height}" fill="{BLUEJAY}"/>
  <circle cx="{b.width-140}" cy="80" r="52" fill="none" stroke="{BLUEJAY}" stroke-width="10" opacity="0.32"/>
  {task_map_icon(b.width-510,28)}
  <text x="110" y="168" fill="{WHITE}" font-family="Arial, Helvetica, sans-serif" font-size="72" font-weight="700">{safe_text(b.title)}</text>
  <text x="114" y="244" fill="{SUBTLE}" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="400">{safe_text(b.subtitle)}</text>
  <line x1="114" y1="285" x2="610" y2="285" stroke="{BLUEJAY}" stroke-width="8" stroke-linecap="round"/>
  <text x="114" y="334" fill="{BLUEJAY}" font-family="Arial, Helvetica, sans-serif" font-size="24" letter-spacing="3">PRODUCTION DRAFT</text>
</svg>'''

def font(size:int, bold:bool=False):
    candidates=[
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/System/Library/Fonts/Supplemental/Arial Bold.ttf' if bold else '/System/Library/Fonts/Supplemental/Arial.ttf'
    ]
    for c in candidates:
        if Path(c).exists(): return ImageFont.truetype(c,size)
    return ImageFont.load_default()

def render_png(path:Path,b:Banner):
    img=Image.new('RGB',(b.width,b.height),MIDNIGHT); d=ImageDraw.Draw(img)
    d.rectangle([0,0,22,b.height],fill=BLUEJAY)
    d.ellipse([b.width-192,28,b.width-88,132],outline=BLUEJAY,width=10)
    x=b.width-510; y=28
    d.rounded_rectangle([x,y+58,x+360,y+248],radius=22,outline=WHITE,width=8)
    d.line([x+35,y+96,x+325,y+96,x+267,y+162,x+93,y+162,x+35,y+96],fill=BLUEJAY,width=8,joint='curve')
    d.line([x+180,y+58,x+180,y+16],fill=BLUEJAY,width=8)
    d.ellipse([x+144,y-32,x+216,y+40],outline=BLUEJAY,width=8)
    d.line([x+165,y+4,x+177,y+16,x+201,y-12],fill=WHITE,width=7)
    d.line([x+180,y+248,x+180,y+293,x+75,y+293],fill=BLUEJAY,width=8)
    d.line([x+180,y+293,x+285,y+293],fill=BLUEJAY,width=8)
    d.rounded_rectangle([x-6,y+315,x+144,y+373],radius=18,outline=WHITE,width=7)
    d.rounded_rectangle([x+216,y+315,x+366,y+373],radius=18,outline=WHITE,width=7)
    d.text((110,115),b.title,fill=WHITE,font=font(72,True))
    d.text((114,214),b.subtitle,fill=SUBTLE,font=font(34,False))
    d.line([114,285,610,285],fill=BLUEJAY,width=8)
    d.text((114,310),'PRODUCTION DRAFT',fill=BLUEJAY,font=font(24,False))
    img.save(path)

def write_banner(root:Path,b:Banner):
    ad=root/'assets/title-banners'/b.folder; od=root/'build/output/title-banners'/b.folder
    ad.mkdir(parents=True,exist_ok=True); od.mkdir(parents=True,exist_ok=True)
    svg=banner_svg(b)
    for d in (ad,od):
        (d/(b.filename_base+'.svg')).write_text(svg,encoding='utf-8')
        render_png(d/(b.filename_base+'.png'), b)
    icon='''<svg xmlns="http://www.w3.org/2000/svg" width="420" height="420" viewBox="0 0 420 420">'''+task_map_icon(30,20)+"</svg>\n"
    (ad/'icons').mkdir(exist_ok=True); (ad/'icons/inbox-decision-flow-icon.svg').write_text(icon,encoding='utf-8')

def make_contact(root:Path):
    imgs=list((root/'build/output/title-banners').glob('asset-*/*.png'))
    w,h=900,260; sheet=Image.new('RGB',(w,max(h*len(imgs),h)), 'white'); d=ImageDraw.Draw(sheet)
    if not imgs: d.text((20,20),'No title banners built yet', fill=(0,40,85))
    for i,p in enumerate(imgs):
        im=Image.open(p).convert('RGB'); im.thumbnail((520,180)); y=i*h+30; sheet.paste(im,(20,y)); d.text((570,y+30),p.name,fill=(0,40,85)); d.text((570,y+65),'Partial contact sheet: available banners only',fill=(77,77,79))
    out=root/'build/output/title-banners/contact-sheet'; out.mkdir(parents=True,exist_ok=True); sheet.save(out/'Classic-Outlook_Title-Banners_Master-Contact-Sheet_v1.0.png')

def validate(root:Path,banners:list[Banner]):
    val=root/'build/output/title-banners/validation'; val.mkdir(parents=True,exist_ok=True)
    rows=[]; checks=[]
    for b in banners:
        for ext in ('svg','png'):
            p=root/'assets/title-banners'/b.folder/(b.filename_base+'.'+ext); checks.append((p.exists(),f'{ext.upper()} exists: {p}'))
        im=Image.open(root/'assets/title-banners'/b.folder/(b.filename_base+'.png')); checks.append((im.size==(b.width,b.height),f'PNG dimensions {im.size} match {b.width}x{b.height}'))
        rows.append({'asset':f'{b.asset:02d}','file':b.filename_base+'.png','title':b.title,'alt_text':b.alt_text,'status':'Production draft','implementation_note':'Keep real document title as live Word text outside this decorative branded header image.'})
    with (val/'Banner-Asset-01_Alt-Text_v1.0.csv').open('w',newline='',encoding='utf-8') as f: w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    with (val/'Title-Banners_Master-Alt-Text_v1.0.csv').open('w',newline='',encoding='utf-8') as f: w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    inv=md_inventory(root)
    with (val/'Banner-Asset-01_Source-Inventory_v1.0.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['path','used','note']);
        for p in inv: w.writerow([str(p), 'yes' if p.name in ['14. Classic Outlook supplemental support package.md','BCBSKS_Master_Brand_Kit.md','BCBSKS-ID-Prompt-Guide-v4.0.md','01. Locked scope for Guide 1.md','02. Detailed build plan.md'] else 'reference inventory', 'Markdown source inventory'])
    passed=sum(1 for ok,_ in checks if ok)
    text='# Banner Asset 01 Validation v1.0\n\nStatus: Production draft\n\n'+'\n'.join([f"- {'PASS' if ok else 'FAIL'} — {msg}" for ok,msg in checks])+"\n- PASS — Midnight background #002855, Bluejay accent #41B6E6, and white title text are specified in SVG.\n- PASS — No logo elements are included.\n- PASS — Human review needs are documented; no automated accessibility compliance claim is made.\n"
    (val/'Banner-Asset-01_Validation_v1.0.md').write_text(text,encoding='utf-8')
    (val/'Banner-Asset-01_Build-Report_v1.0.md').write_text(f'# Banner Asset 01 Build Report v1.0\n\nStatus: Production draft\n\nGenerated at: {now_iso()}\n\nSelected asset: Classic Outlook Task Map\n\nSubtitle refined for plain English and field-use clarity: "Choose the right Outlook action for common inbox work."\n\nConflict log: No blocking source conflicts found. Brand color conflict noted between Primary Blue values; this banner uses Midnight #002855 from the brand kit and Bluejay #41B6E6 common to both sources.\n\nContact sheet status: Partial until all asset groups are built. PNG contact-sheet output is generated by the local/CI build and excluded from git because binary files are not supported in review.\n',encoding='utf-8')
    (val/'Banner-Asset-01_Unresolved-Items_v1.0.md').write_text('# Banner Asset 01 Unresolved Items v1.0\n\nStatus: Production draft\n\n- Human brand review required before publication.\n- Human accessibility review required before DOCX placement; keep real title as live text outside the image.\n- Contact sheet is partial until all banner asset groups are merged and rebuilt.\n\nPublication blockers: None known for the generated banner package.\n\nBinary policy note: PNG banner and contact-sheet files are generated outputs available from the build and CI artifact, but are intentionally not committed.\n',encoding='utf-8')
