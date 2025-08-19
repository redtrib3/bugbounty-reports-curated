# Worker container escape lead to arbitrary file reading in host machine [again]

**Target**: Semmle

**Reported on**: hackerone

**Bug Type**: path traversal

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/697055

## Summary
The researcher discovered that when both `lgtm.yml` and `.lgtm.yml` exist in a project, LGTM processes only `lgtm.yml` but keeps `.lgtm.yml` in the build directory. By creating a symlink named `.lgtm.yml` pointing to a host machine file, an attacker can cause LGTM to expose arbitrary host files after a successful build (e.g., /etc/passwd). This enables sensitive information disclosure from the underlying host.

## Bounty received ($)
2000

## References
- https://hackerone.com/reports/697055
## Tags
- path-traversal
- privilege-escalation
