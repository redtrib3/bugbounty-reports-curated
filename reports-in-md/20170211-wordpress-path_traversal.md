# Wordpress unzip_file path traversal

**Target**: Wordpress

**Reported on**: hackerone

**Bug Type**: path traversal

**Severity**: Medium

**Report URL**: https://hackerone.com/reports/205481

## Summary
A researcher found out that the wordpress `unzip_file` function was vulnerable to path traversal as it enabled any attacker to overwrite any file in writable path using '../<filepath to overwrite>'. 
The vulnerability existed as the `$to` parameter unzipped the file into any path without normalization of the input. The patch of this vulnerability was released in 4.8.2 (7 months since reporting.)

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/205481
## Tags
- path-traversal
- violation-of-secure-design-principal
