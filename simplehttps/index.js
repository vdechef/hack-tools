var express = require('express')
var fs = require('fs')
var https = require('https')
var app = express()

const PORT=443

app.all('*', function (req, res) {
    console.log(
        JSON.stringify({
            method: req.method,
            url: req.url,
            timestamp: Date.now(),
            rawHeaders: req.rawHeaders,
            httpVersion: req.httpVersion,
            remoteAddress: req.remoteAddress,
            remoteFamily: req.remoteFamily,
            body: req.body
        }, null, 4)
      );
    res.send('hello world')
})

https.createServer({
    key: fs.readFileSync('./certs/privkey.pem'),
    cert: fs.readFileSync('./certs/cert.pem')
}, app)
.listen(PORT, function () {
    console.log('Example app listening on https://localhost:'+PORT)
})
