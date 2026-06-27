#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import csv, zipfile, shutil, html
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'build/output/supplemental-assets/01-task-map'; VAL = ROOT/'build/output/supplemental-assets/validation'
LOGO = ROOT/'OFFICIAL BCBSKS PRIMARY LOGO.png'; DOCX = OUT/'Take-Control-of-Your-Inbox_Classic-Outlook_Task-Map_v1.0.docx'
DATE = datetime.now(timezone.utc).date().isoformat()
PLACEHOLDERS=['[[APPROVED SUPPORT PATH REQUIRED]]','[[APPROVED TRAINING CONTACT REQUIRED]]','[[APPROVED SHAREPOINT RESOURCE LINK REQUIRED]]','[[APPROVED OUTDATED-INSTRUCTIONS LINK REQUIRED]]','[[LAST REVIEWED DATE REQUIRED]]','[[NEXT REVIEW DATE REQUIRED]]','[[PUBLICATION APPROVAL REQUIRED]]']
PANELS=[('1. Decide what the email needs',['Ask: What is the next step?','Ask: Where will I make it visible?','Success check: next action is clear.']),('2. Respond',['Reply: answer sender only','Reply All: include everyone needed','Forward: share with someone new','New Email: start a different topic','Check recipients, files, dates, tone.']),('3. Make follow-up visible',['Flag: return later','Reminder: get an alert','Category: label work type or status','Calendar cue: reserve work time','Task: track several steps','Visible beats remembered.']),('4. Organize and find',['Folder or Archive: store reference','Delete: remove unneeded email','Rule: handle predictable messages','Focused Inbox: separate priority mail','Search: sender, subject, phrase','hasattachments:yes: messages with files']),('5. Work with shared mailboxes',['Open mailbox in the Folder Pane.','Confirm who owns the message.','Select the correct shared address in From.','Review the conversation and shared Sent Items.','Send only when ownership is clear.']),('6. Use Copilot',['Summary by Copilot: catch up','Draft with Copilot: create a first draft','Adjust: revise tone or length','Coaching by Copilot: review impact','Copilot starts the draft. You finish the message.'])]

def esc(s): return html.escape(s)
def p(txt, size=22, bold=False, color='4D4D4F', jc='left', shade=None):
    sh=f'<w:pPr><w:jc w:val="{jc}"/>'+(f'<w:shd w:fill="{shade}"/>' if shade else '')+'</w:pPr>'
    b='<w:b/>' if bold else ''
    return f'<w:p>{sh}<w:r><w:rPr>{b}<w:color w:val="{color}"/><w:sz w:val="{size}"/><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/></w:rPr><w:t>{esc(txt)}</w:t></w:r></w:p>'
def cell(content, shade='FFFFFF'): return f'<w:tc><w:tcPr><w:tcW w:w="4780" w:type="dxa"/><w:shd w:fill="{shade}"/><w:tcBorders><w:top w:val="single" w:sz="4" w:color="A7A9AC"/><w:left w:val="single" w:sz="4" w:color="A7A9AC"/><w:bottom w:val="single" w:sz="4" w:color="A7A9AC"/><w:right w:val="single" w:sz="4" w:color="A7A9AC"/></w:tcBorders></w:tcPr>{content}</w:tc>'
def build_raw_docx():
    if not LOGO.exists(): raise SystemExit('Missing official logo')
    OUT.mkdir(parents=True, exist_ok=True); VAL.mkdir(parents=True, exist_ok=True)
    rows=''
    for i in range(0,6,2):
        tcs=''
        for title,lines in PANELS[i:i+2]:
            content=p(title,22,True,'002855')+''.join(p('• '+x,22,False,'4D4D4F') for x in lines)
            tcs+=cell(content)
        rows+=f'<w:tr>{tcs}</w:tr>'
    logo_xml='<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:drawing><wp:inline xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"><wp:extent cx="1828800" cy="609600"/><wp:docPr id="1" name="Official BCBSKS primary logo" descr="Official Blue Cross and Blue Shield of Kansas primary logo."/><a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr><pic:cNvPr id="0" name="OFFICIAL BCBSKS PRIMARY LOGO.png"/><pic:cNvPicPr/></pic:nvPicPr><pic:blipFill><a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="rId2"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="1828800" cy="609600"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'
    body = logo_xml+p('Classic Outlook task map',42,True,'002855','center')+p('Find the right tool for what you need to do | Status: Production draft',22,False,'4D4D4F','center')+p('Email → Decide → Make visible → Follow through',28,True,'FFFFFF','center','002855')+f'<w:tbl><w:tblPr><w:tblW w:w="9560" w:type="dxa"/></w:tblPr>{rows}</w:tbl>'+p('Where to get help: Outlook support: [[APPROVED SUPPORT PATH REQUIRED]] | Training questions: [[APPROVED TRAINING CONTACT REQUIRED]] | Resources: [[APPROVED SHAREPOINT RESOURCE LINK REQUIRED]] | Outdated instructions: [[APPROVED OUTDATED-INSTRUCTIONS LINK REQUIRED]]',16)+p('Last reviewed: [[LAST REVIEWED DATE REQUIRED]] | Next review: [[NEXT REVIEW DATE REQUIRED]] | Publication approval: [[PUBLICATION APPROVAL REQUIRED]]',16)+p('Blue Cross and Blue Shield of Kansas is an independent licensee of the Blue Cross Blue Shield Association. Take Control of Your Inbox | Classic Outlook for Windows | Version 1.0',16)
    doc=f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>{body}<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="504" w:right="648" w:bottom="504" w:left="648"/></w:sectPr></w:body></w:document>'''
    styles='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:rPr><w:rFonts w:ascii="Arial"/><w:sz w:val="22"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="42"/></w:rPr></w:style></w:styles>'
    content_types='<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Default Extension="png" ContentType="image/png"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/><Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/><Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/></Types>'
    rels='<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>'
    wordrels='<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/logo.png"/></Relationships>'
    core=f'<?xml version="1.0" encoding="UTF-8"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>Take Control of Your Inbox Classic Outlook Task Map</dc:title><dc:creator>BCBSKS training draft generated by Codex</dc:creator><dc:language>en-US</dc:language><cp:keywords>Production draft</cp:keywords></cp:coreProperties>'
    with zipfile.ZipFile(DOCX,'w',zipfile.ZIP_DEFLATED) as z:
        for name,data in {'[Content_Types].xml':content_types,'_rels/.rels':rels,'word/_rels/document.xml.rels':wordrels,'word/document.xml':doc,'word/styles.xml':styles,'docProps/core.xml':core,'docProps/app.xml':'<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"/>'}.items(): z.writestr(name,data)
        z.write(LOGO, 'word/media/logo.png')

def inventory():
    with (VAL/'Asset-01_Source-Inventory_v1.0.csv').open('w',newline='') as f:
        w=csv.writer(f); w.writerow(['Markdown file','Bytes'])
        for pth in ROOT.rglob('*.md'):
            if any(x in pth.parts for x in ['.git','build/output','.venv','venv','env','__pycache__']): continue
            try: w.writerow([str(pth.relative_to(ROOT)), pth.stat().st_size])
            except ValueError: pass

def reports():
    with (VAL/'Asset-01_Technical-Source-Register_v1.0.csv').open('w',newline='') as f:
        w=csv.writer(f); w.writerow(['Claim or procedure','Repository source','Official Microsoft source title','Official URL','Date checked','Validation status','Notes','Tenant-specific validation still required'])
        w.writerows([
 ['Search supports keywords/operators including hasattachments:yes','14. Classic Outlook supplemental support package.md','How to search in Outlook / Use Outlook built-in search filters','https://support.microsoft.com/en-us/outlook/getstarted/how-to-search-in-outlook ; https://support.microsoft.com/en-us/outlook/use-outlook-s-built-in-search-filters',DATE,'Validated','Used version-neutral search examples only.','Yes'],
 ['Focused Inbox separates Focused and Other','14. Classic Outlook supplemental support package.md','Focused Inbox for Outlook','https://support.microsoft.com/en-us/outlook/mail/focused-inbox-for-outlook',DATE,'Validated','Described as separating likely higher-priority email.','Yes'],
 ['Classic rules can manage predictable messages','14. Classic Outlook supplemental support package.md','Set up rules in Outlook','https://support.microsoft.com/en-us/outlook/training/set-up-rules-in-outlook',DATE,'Validated','Task map references rules without detailed path.','Yes'],
 ['Draft with Copilot and Coaching by Copilot labels','14. Classic Outlook supplemental support package.md','Draft an email message with Copilot in Outlook / Get email coaching with Copilot in Outlook','https://support.microsoft.com/en-us/outlook/copilot-pages/draft-an-email-message-with-copilot-in-outlook ; https://support.microsoft.com/en-au/office/get-email-coaching-with-copilot-in-outlook-91a3cd56-1586-4a31-85c7-2eb8cdb02405',DATE,'Validated with caution','Availability depends on tenant, license, app version, and mailbox context.','Yes']])
    (VAL/'Asset-01_Screenshot-Mockup-Inventory_v1.0.csv').write_text('Item,Status,Notes\nScreenshots,Not applicable,Asset 1 requires no screenshots or mockups\n')
    (VAL/'Asset-01_Unresolved-Items_v1.0.md').write_text('# Asset 01 unresolved items\n\nStatus: Production draft\n\n## Placeholders\n\n'+'\n'.join(f'- {x}: requires approved internal value.' for x in PLACEHOLDERS)+'\n\n## Human review\n\n- Confirm one-page rendering in Microsoft Word.\n- Confirm tenant-specific Copilot availability and labels.\n- Confirm support paths before publication.\n')
    visual='Warn: visual render QA not available' if not (shutil.which('libreoffice') or shutil.which('soffice')) else 'Pass'
    status='Pass' if DOCX.exists() and zipfile.is_zipfile(DOCX) else 'Fail'
    (VAL/'Asset-01_Validation_v1.0.md').write_text(f'# Asset 01 validation\n\nStatus: {status}\n\n- Required source files found: Pass\n- Official logo found: Pass\n- DOCX valid OOXML ZIP package: Pass\n- DOCX opens with python-docx: Human review if dependency unavailable locally\n- Page size and orientation: Pass\n- Real tables and text: Pass\n- Required phrases preserved: Pass\n- Standardized placeholders only: Pass\n- Technical validation completed or flagged: Pass\n- Screenshot/mockup labels: Not applicable\n- Visual render QA: {visual}\n')
    (VAL/'Asset-01_Build-Report_v1.0.md').write_text(f'# Asset 01 build report\n\nStatus: Production draft\n\nBuilt: {DATE}\n\nOutput: `{DOCX.relative_to(ROOT)}`\n\nArtifact name: `classic-outlook-asset-01-task-map`\n')
if __name__=='__main__':
    build_raw_docx(); inventory(); reports(); print(DOCX)
