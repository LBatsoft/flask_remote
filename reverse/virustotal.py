import execjs
import requests

js = """
function get_anti() {
    const e = Date.now() / 1e3;
    return Buffer.from((`${(()=>{
        const e = 1e10 * (1 + Math.random() % 5e4);
        return e < 50 ? "-1" : e.toFixed(0)
    }
    )()}-ZG9udCBiZSBldmls-${e}`)).toString('base64');
}
"""

xvt_anti = execjs.compile(js).call('get_anti')
print(xvt_anti)

import requests

headers = {
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'x-app-version': 'v1x239x0',
    'X-Tool': 'vt-ui-main',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json',
    'Referer': 'https://www.virustotal.com/',
    'Accept-Ianguage': 'en-US,en;q=0.9,es;q=0.8',
    'X-VT-Anti-Abuse-Header': xvt_anti,
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://www.virustotal.com/ui/ip_addresses/127.0.0.1', headers=headers)
print(response.json())