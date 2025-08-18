# HTTP Request Smuggling on https://labs.data.gov

**Target**: GSA Bounty

**Reported on**: hackerone

**Bug Type**: HTTP request smuggling

**Severity**: High

**Report URL**: https://hackerone.com/reports/726773

## Summary
The researcher found an HTTP request smuggling (TE.CL) vulnerability in an application where the frontend uses Transfer encoding header and the backend uses Content Length.
To reproduce the vulnerability the reporter had set a POST request to '/' followed by a POST request to '/hopefully404', the reported also made sure to send a batch of request after 
to prevent the attack affecting innocent users. The attacker url was reportedly reflected in the response html as well.

## Bounty received ($)
750

## References
- https://hackerone.com/reports/726773
## Tags
- http-request-smuggling
- http1.1-must-die
- desync
