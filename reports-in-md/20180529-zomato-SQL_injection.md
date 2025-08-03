# Boolean-Blind SQLi on `order_id` parameter

**Target**: Zomato

**Reported on**: hackerone

**Bug Type**: SQL Injection (Boolean-based Blind)

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/358669

## Summary
There was an endpoint called `order_id` in zomato's website that was vulnerable to Boolean-based Blind SQL injection.
Requesting `order_id='-if(1=2,'0','1')-'` changed the response length and on further investigation from the researcher,
found out that the data could be dumped, using automated tools such as SQLmap.

## Bounty received ($)
1000

## References
- https://hackerone.com/reports/358669
## Tags
- sqli
- boolean-based
- blind-sqli
