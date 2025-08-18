# Mass account takeovers using HTTP Request Smuggling on https://slackb.com/ to steal session cookies

**Target**: Slack

**Reported on**: hackerone

**Bug Type**: HTTP request smuggling

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/737140

## Summary
The researcher exploited an HTTP Request Smuggling bug on a Slack asset to perform a CL.TE-based hijack onto neighboring customer requests. This hijack forced the victim into an open-redirect that forwarded the victim onto the researcher's collaborator client with slack domain cookies. The posted cookies in the customer request on the collaborator client contained the customer's secret session cookie. With this attack the researcher was able to prove session takeover against arbitrary slack customers.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/737140
## Tags
- http-request-smuggling
- http1.1-must-die
- desync
