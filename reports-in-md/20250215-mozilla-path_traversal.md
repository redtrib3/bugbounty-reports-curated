# Mozilla VPN Clients: RCE via file write and path traversal

**Target**: Mozilla

**Reported on**: hackerone

**Bug Type**: Path Traversal

**Severity**: High

**Report URL**: https://hackerone.com/reports/2995025

## Summary
In Mozilla VPN Client, there is a feature to enable developer mode in settings. This has the inspector feature that runs a websocket in ws://localhost:8765 - this is for debugging purpose. 
The WebSocket accepts a `live_reload` command that takes in a url staging any file, whatever file we pass in will be saved to the localpath: 
%LOCALAPPDATA%\Mozilla\Mozilla VPN\hot_reload\

An attacker can stage a http server serving a file with the name "..\\..\\test.dll", which will save it two directories behind. This can be leveraged to achieve code execution.

## Bounty received ($)
6000

## References
- https://hackerone.com/reports/2995025
- https://www.mozilla.org/en-US/products/vpn/download/
- https://github.com/mozilla-mobile/mozilla-vpn-client/blob/main/src/inspector/inspectorhotreloader.cpp
## Tags
- path-traversal
- remote-code-execution
- websocket
- local-file-write
- developer-feature-abuse
- client-side
