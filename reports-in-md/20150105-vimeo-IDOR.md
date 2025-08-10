# Vimeo.com Insecure Direct Object References Reset Password

**Target**: Vimeo

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/42587

## Summary
The researcher found a vulnerability in the password reset functionality through which an attacker can reset anyone's password by knowning the numerical userid of user.
The user id is easily obtainable from vimeo's public API. The password reset was in format - `https://vimeo.com/forgot\_password/[user id]/[token]`, By simply replacing the userid with the id of other user,
one could takeover any account.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/42587
## Tags
- IDOR
- broken-access-control
- password-reset
