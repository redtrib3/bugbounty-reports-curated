# Hacker.one subdomain takeover

**Target**: hackerone

**Reported on**: hackerone

**Bug Type**: subdomain takeover

**Severity**: Low

**Report URL**: https://hackerone.com/reports/159156

## Summary
The researcher found a subdomain takeover vulnerability in one of the domains owned by hackerone - hacker.one.
On visiting the hacker.one domain, the researcher was hit with an Instapage error page. Instapage is a service that
lets you build landing pages for your online marketing campaigns. It allows users to map its templates to their own domain or subdomain.

For some reason, the subdomain had a lingering CNAME record pointing to Instapage even after the service had been discontinued.
Instapage did not verify domain ownership during page creation, which allowed the researcher to claim the abandoned endpoint
and publish arbitrary content under hacker.one's subdomain. This is a classic subdomain takeover scenario.

Although no sensitive data exposure occurred, such takeovers can be used for phishing, brand impersonation, or reputational damage.
The issue was reported and resolved by removing the DNS mapping from the Instapage side.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/159156
- http://www.geekboy.ninja/blog/hijacking-tons-of-instapage-expired-users-domains-subdomains/
## Tags
- secure-design-principle-violation
- subdomain-takeover
