# Subdomain takeover on developer.openapi.starbucks.com

**Target**: starbucks

**Reported on**: hackerone

**Bug Type**: Subdomain takeover

**Severity**: High

**Report URL**: https://hackerone.com/reports/275714

## Summary
The researcher found out that the endpoint - developer.openapi.starbucks.com returned 200 status code response with body containing the text: 'Unrecognized domain: developers.starbucks.com',
the server header indicated that it was hosted in www.mashery.com, the researcher registered and added the domain to his page and was able to host his own content from that domain.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/275714
## Tags
- subdomain-takeover
