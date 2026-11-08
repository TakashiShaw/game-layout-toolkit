"""Reproducible MCP protocol client; saves request and full tool response."""
import asyncio, json, os, sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    label=sys.argv[1]
    clicks=sys.argv[2:]
    root=Path(__file__).resolve().parent
    params=StdioServerParameters(command=sys.executable,args=[str(root/'server.py')],env=dict(os.environ))
    async with stdio_client(params) as (read,write):
        async with ClientSession(read,write) as client:
            await client.initialize()
            names=[t.name for t in (await client.list_tools()).tools]
            assert names==['inspect_game_layout'],names
            request={'url':os.environ.get('GAME_URL','http://127.0.0.1:8138/?dev=1&manual=1'),'game_selector':'#game','clicks':clicks}
            result=await client.call_tool('inspect_game_layout',request)
            record={'tool':'inspect_game_layout','request':request,'response':result.model_dump(mode='json')}
            (root/'evidence'/f'{label}-mcp.json').write_text(json.dumps(record,indent=2))
            if result.is_error:
                raise RuntimeError(str(result.content))
            data=result.structured_content
            if data is None:
                data=json.loads(next(c.text for c in result.content if hasattr(c,'text')))
            print(json.dumps({'label':label,'reportPath':data.get('reportPath'),'viewports':[{k:r.get(k) for k in ('name','coverage','document','error')} for r in data.get('results',[])]},indent=2))
if __name__=='__main__': asyncio.run(main())
