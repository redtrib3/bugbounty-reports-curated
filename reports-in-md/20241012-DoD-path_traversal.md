# Unauthenticated LFI (Local File Inclusion) using the symbol `!`

**Target**: U.S. Dept Of Defense

**Reported on**: hackerone

**Bug Type**: path traversal

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/2778380

## Summary
The researcher found that the Jolokia endpoint `/jolokia/exec/com.sun.management:type=DiagnosticCommand/compilerDirectivesAdd/` is vulnerable to path traversal using `!` in directory names. This allows an unauthenticated attacker to read arbitrary local files on the server, including sensitive system files like /etc/passwd and /etc/crontab, potentially exposing configuration and application secrets.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/2778380
## Tags
- path-traversal
- violation-of-secure-design-principal
