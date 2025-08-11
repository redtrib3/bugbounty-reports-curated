# Subdomain Takeover Via Insecure CloudFront Distribution cdn.grab.com

**Target**: Grab

**Reported on**: hackerone

**Bug Type**: Subdomain takeover

**Severity**: Medium

**Report URL**: https://hackerone.com/reports/352869

## Summary
The researcher found a subdomain takeover vulnerability in cdn.grab.com which had a dangling CNAME pointing to a cloudfront instance.
The subdomain was not registered on amazon Aws Cloudfront. The researcher was able to successfully takeover the domain by registering a cloudfront subdomain.

## Bounty received ($)
1000

## References
- https://hackerone.com/reports/352869
## Tags
- subdomain-takeover
