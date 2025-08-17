# Account deletion using the /v1/account/destroy API endpoint using account password without 2FA verification

**Target**: Mozilla

**Reported on**: hackerone

**Bug Type**: MFA

**Severity**: Medium

**Report URL**: https://hackerone.com/reports/2197244

## Summary
The account deletion endpoint at POST /v1/account/destroy does not check for 2FA and doesn't require an authorization header. Therefore, an unauthenticated attacker who knows the password of a user can delete their account without the need of 2FA.
The reported was able to show more impact by providing information that the ratelimiting is implemented on a account basis and not IP, and also availablility of a new 1 Billion+ credential breach data on Firefox during that time.

## Bounty received ($)
1000

## References
- https://hackerone.com/reports/2197244
## Tags
- 2FA
- MFA-bypass
