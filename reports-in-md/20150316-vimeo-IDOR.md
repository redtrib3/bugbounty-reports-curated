# Insecure Direct Object References that allows to read any comment (even if it should be private)

**Target**: Vimeo

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: Unspecified

**Report URL**: https://hackerone.com/reports/52181

## Summary
The researcher found an IDOR vulnerablity that enabled a user to reveal private comments on a video by just knowing its comment ID - knowing comment_id is a precondition.
This is by editing an attacker posted comment from attacker account, intercepting the request and changing the comment_id get parameter in the request `GET /122303200?comment_id=<CHANGE_THIS>&is_sticky=0&action=comment_edit_form HTTP/1.1`.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/52181
## Tags
- IDOR
