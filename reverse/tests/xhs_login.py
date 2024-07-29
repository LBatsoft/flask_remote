import requests

cookies = {
    'abRequestId': 'd61b08cf-2ce5-54d8-9e43-50a5eaf5098d',
    'a1': '18fe7381f3e6ejl32dm9ms1zth75kx05au5t4lfq230000294719',
    'webId': '3274f1c8928dabed41ec298e708139ed',
    'gid': 'yYidWqYJWJ0yyYidWqYyi71iqdKdV1qJf6j62AJMyu9xW9q82TC824888Jj4Wyj8Jydy2dfq',
    'xsecappid': 'xhs-pc-web',
    'web_session': '030037a1a570210bd30c1962ee214a6308743e',
    'webBuild': '4.25.1',
    'websectiga': '82e85efc5500b609ac1166aaf086ff8aa4261153a448ef0be5b17417e4512f28',
    'sec_poison_id': '804ab67f-96b0-4b8c-bc09-52c1d82eb374',
    'acw_tc': '7d8a139a5c52a58e5bcb1ac548e22b014303bb93da8ebd7e8ce7ae6ac45f3995',
    'unread': '{%22ub%22:%2266897887000000001e012f62%22%2C%22ue%22:%226675c916000000001c02aabe%22%2C%22uc%22:25}',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'x-t': '1721188083291',
    'x-b3-traceid': '68ea59aa002b999c',
    'sec-ch-ua-mobile': '?0',
    '_x_-s-common': '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',
    '_x_-s': 'XYW_eyJzaWduU3ZuIjoiNTIiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6IjAyMjJjODI0N2UzYTk1OTBjYzA1Y2VkZTBiOTYwMjE4ZWYwNTM1YTMzMjEzYzc0MjgzYjNiMmI3ZTY2NTQ3ZTMzNDk4NTFmNTVmMzBiM2U2Y2ZhYzMyNjZiYTNkYWFkNGQwNTc1MDMwNTY2NTA0MjE4ODgxNDNkOWFkNGRkYmQ5ODg4MTQzZDlhZDRkZGJkOWI1NmNjM2EzN2M2YTdhYWRlOTM2NTBhZGMzMzlkZTY0MGQwNzFlMjA5ZjczODE2MTUxOWRiOWM0ODJlODMwNjc5ZDUxYTZhYjhkOWI4NWI5ZDAyOWYyMGM1ZjlkMzc2ZTZhZGQ4YTU2MzIxN2JkMTY3MTBiOWY5ZjNiYjZiNWY2YzQxZjU3YmZlNGJmZWNmYTMzZDU0OTU3OGVmMTIzZDIxODgzZWIyNWU2Nzg3ZGMzOTFjZGVjNzk5ODQ3MGRlMzE5NmNmYmVmY2JiZDNkOTMxNDVjZDkxNDE2NzFmN2ZkMjdmMDIwMDg4MDUyNzY5NCJ9',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://www.xx.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.xx.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=1, i',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'abRequestId=d61b08cf-2ce5-54d8-9e43-50a5eaf5098d; a1=18fe7381f3e6ejl32dm9ms1zth75kx05au5t4lfq230000294719; webId=3274f1c8928dabed41ec298e708139ed; gid=yYidWqYJWJ0yyYidWqYyi71iqdKdV1qJf6j62AJMyu9xW9q82TC824888Jj4Wyj8Jydy2dfq; xsecappid=xhs-pc-web; web_session=030037a1a570210bd30c1962ee214a6308743e; webBuild=4.25.1; websectiga=82e85efc5500b609ac1166aaf086ff8aa4261153a448ef0be5b17417e4512f28; sec_poison_id=804ab67f-96b0-4b8c-bc09-52c1d82eb374; acw_tc=7d8a139a5c52a58e5bcb1ac548e22b014303bb93da8ebd7e8ce7ae6ac45f3995; unread={%22ub%22:%2266897887000000001e012f62%22%2C%22ue%22:%226675c916000000001c02aabe%22%2C%22uc%22:25}',
}

params = {
    'phone': '16619712228',
    'zone': '86',
    'type': 'login',
}

response = requests.get('https://xxx.com/api/sns/web/v2/login/send_code', params=params, cookies=cookies, headers=headers)

print(response.json())