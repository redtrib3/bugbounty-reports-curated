# Github access token exposure

**Target**: shopify

**Reported on**: hackerone

**Bug Type**: sensitive data exposure

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/1087489

## Summary
A researcher on testing desktop macOS application found a env file which wasn't used by the application
On further investigation, the .env file contained a github PAT owned by a shopify employee and has Read-Write access on Shopify production github repository.

## Bounty received ($)
50000

## References
- https://hackerone.com/reports/1087489
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
## Tags
- sensitive-data-exposure
- cryptographic-failure
- misconfiguration
