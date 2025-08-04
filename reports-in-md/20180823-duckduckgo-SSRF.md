# SSRF on duckduckgo.com/iu/

**Target**: DuckDuckGo

**Reported on**: hackerone

**Bug Type**: SSRF

**Severity**: High

**Report URL**: https://hackerone.com/reports/398641

## Summary
The researcher on testing noticed a parameter `u` in https://duckduckgo.com/iu?u=yimg.com with the value `yimg.com` being sent randomly.
Any other domain other than yimg.com being there, returned an error. the vulnerability was that the `u` parameter was simply checking for the existence of the yimg.com string in the parameter `u` value.
This resulted in a SSRF as it enables an attacker to access internal resources, or request external website (all you have to do is add the yimg as a string to the malicious `u` value.)
This also has the potential for  Cross-site-port scanning attack.

## Bounty received ($)
swag

## References
- https://hackerone.com/reports/398641
## Tags
- SSRF
- XSPA
- information-disclosure
