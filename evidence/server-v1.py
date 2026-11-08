"""Local browser-game measurements exposed as one MCP tool."""
import json
import os
import uuid
from pathlib import Path
from urllib.parse import urlparse
from mcp.server.mcpserver import MCPServer
from playwright.async_api import async_playwright

mcp = MCPServer('game-layout')
SIZES = [('phone-portrait',390,844),('phone-landscape',844,390),
         ('tablet-portrait',768,1024),('tablet-landscape',1024,768),
         ('laptop',1366,768),('desktop',1920,1080)]
ROOT = Path(os.environ.get('GAME_LAYOUT_OUTPUT', str(Path(__file__).parent / 'evidence'))).resolve()

MEASURE = r'''selector => {
 const game = document.querySelector(selector);
 if (!game) throw new Error('Game selector not found: '+selector);
 const rect = el => {const r=el.getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height,right:r.right,bottom:r.bottom};};
 const visible = el => {const r=el.getBoundingClientRect(),s=getComputedStyle(el);return r.width>0&&r.height>0&&s.visibility!=='hidden'&&s.display!=='none'&&!el.closest('[hidden]');};
 const name = el => el.id ? '#'+el.id : el.tagName.toLowerCase()+'.'+[...el.classList].join('.');
 const controls=[...document.querySelectorAll('button,summary,a[href],input,select')].filter(visible).map(el=>{
 const r=rect(el);return {selector:name(el),text:(el.innerText||el.getAttribute('aria-label')||'').trim().slice(0,90),...r,insideGame:game.contains(el),fontSize:parseFloat(getComputedStyle(el).fontSize),offscreen:r.x<0||r.y<0||r.right>innerWidth+1||r.bottom>innerHeight+1};});
 const r=rect(game),d=document.documentElement;
 return {viewport:{width:innerWidth,height:innerHeight},game:r,
 coverage:Math.round(Math.max(0,Math.min(r.right,innerWidth)-Math.max(r.x,0))*Math.max(0,Math.min(r.bottom,innerHeight)-Math.max(r.y,0))/(innerWidth*innerHeight)*1000)/10,
 document:{width:d.scrollWidth,height:d.scrollHeight,horizontalOverflow:d.scrollWidth>innerWidth+1,verticalOverflow:d.scrollHeight>innerHeight+1},controls,
 images:[...game.querySelectorAll('img')].filter(visible).map(el=>({selector:name(el),...rect(el),naturalWidth:el.naturalWidth,naturalHeight:el.naturalHeight,objectFit:getComputedStyle(el).objectFit})),
 outsideText:[...document.querySelectorAll('body p,body header,body footer')].filter(el=>visible(el)&&!game.contains(el)).map(el=>({selector:name(el),text:el.innerText.slice(0,150)}))};
}'''

@mcp.tool()
async def inspect_game_layout(url: str, game_selector: str = '#game', clicks: list[str] | None = None) -> dict:
    """Measure a local browser game in six viewport sizes and save screenshots.

    Supply an http URL on localhost/127.0.0.1 and its game-shell CSS selector.
    Optional clicks are ordered CSS selectors to enter gameplay or open menus;
    only use controls on a disposable local game. Each viewport starts fresh.
    Returns geometry, overflow, visible controls, image-fit information, and paths.
    Does not edit source files. Measurements alone do not prove usability.
    """
    parsed=urlparse(url)
    if parsed.scheme != 'http' or parsed.hostname not in ('localhost','127.0.0.1','::1') or parsed.username or parsed.password:
        raise ValueError('Use a local http game URL without credentials.')
    if len(clicks or []) > 8:
        raise ValueError('At most eight state-navigation clicks.')
    folder=ROOT / uuid.uuid4().hex[:12]
    folder.mkdir(parents=True)
    results=[]
    async with async_playwright() as p:
        browser=await p.chromium.launch()
        try:
            for label,w,h in SIZES:
                context=await browser.new_context(viewport={'width':w,'height':h},has_touch=label.startswith(('phone','tablet')),device_scale_factor=1)
                # This inspection is local-only, including subresources and redirects.
                async def guard(route):
                    u=urlparse(route.request.url)
                    if u.scheme in ('data','blob') or (u.scheme=='http' and u.hostname in ('localhost','127.0.0.1','::1')):
                        await route.continue_()
                    else:
                        await route.abort()
                await context.route('**/*',guard)
                page=await context.new_page()
                errors=[]
                page.on('pageerror',lambda e: errors.append(str(e)))
                try:
                    await page.goto(url,wait_until='networkidle',timeout=20000)
                    for selector in clicks or []:
                        await page.locator(selector).click(timeout=5000)
                    await page.evaluate('document.fonts.ready')
                    await page.evaluate('Promise.all([...document.images].map(i=>i.decode().catch(()=>{})))')
                    data=await page.evaluate(MEASURE,game_selector)
                    shot=folder / f'{label}.png'
                    await page.screenshot(path=str(shot))
                    results.append({'name':label,'screenshot':str(shot),'pageErrors':errors,**data})
                except Exception as exc:
                    results.append({'name':label,'error':str(exc),'pageErrors':errors})
                finally:
                    await context.close()
        finally:
            await browser.close()
    report={'url':url,'gameSelector':game_selector,'clicks':clicks or [],'browser':'Playwright Chromium; emulated viewports, not physical-device testing','results':results}
    dest=folder/'report.json'
    dest.write_text(json.dumps(report,indent=2))
    return {'reportPath':str(dest),**report}

if __name__ == '__main__':
    mcp.run(transport='stdio')
