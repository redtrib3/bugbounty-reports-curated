# Path traversal, to RCE

**Target**: Gitlab

**Reported on**: hackerone

**Bug Type**: path traversal

**Severity**: High

**Report URL**: https://hackerone.com/reports/733072

## Summary
The researcher found a path traversal vulnerability in the Gitlab package registry API that allows an attacker to write to any path writable by `git` user, potentially allowing an attacker to write to `authorized_keys` with their public key and get a ssh shell.

## Bounty received ($)
12000

## References
- https://hackerone.com/reports/733072
## Tags
- path-traversal
- violation-of-secure-design-principal
