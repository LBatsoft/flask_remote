var browser = require("browser-tool");

// 解析User-Agent
let info = browser.parse('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0');
console.log(info)
// 获取浏览器详细信息 - 指定字段：'browser','system','device','gpu','network','battery','screen','language','timezone'
let networkInfo =  browser.getInfo(['network']);
console.log(await networkInfo())
// 获取浏览器详细信息 - 全部字段
let info1 =  browser.getInfo();
console.log(await info1())
