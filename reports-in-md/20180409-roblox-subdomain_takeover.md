# Subdomain Takeover to Authentication bypass

**Target**: roblox

**Reported on**: hackerone

**Bug Type**: subdomain takeover

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/335330

## Summary
The researcher discovered that the subdomain devrel.roblox.com pointed to an expired HubSpot instance.
This allowed an attacker to claim the service and take control of the subdomain.
By doing so, the attacker could serve content from a trusted Roblox subdomain, enabling attacks such as cookie theft or authentication bypass.
The researcher demonstrated the impact by showing how authentication could be bypassed using the hijacked subdomain by accessing the  roblox authentication cookies cross domain.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/335330
## Tags
- subdomain-takeover
- authentication-bypass
- cookie-stealing
