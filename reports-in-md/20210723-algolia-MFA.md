# Information disclosure -> 2fa bypass -> POST exploitation

**Target**: algolia

**Reported on**: hackerone

**Bug Type**: MFA

**Severity**: Medium

**Report URL**: https://hackerone.com/reports/1276373

## Summary
The researcher found vulnerability in a webapp that let's an attacker bypass 2FA by knowning a sensitive secret - `gauth_secret` that is leaked on the response when requesting 2FA renew from an account.
The leaked gauth_secret could be used on google authenticator to create codes that can directly be used to pass MFA. Although it doesn't have a direct impact, a account takeover is possible if the gauth_token of a user is leaked somehow.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/1276373
## Tags
- 2FA
- MFA-bypass
