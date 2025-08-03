# Exposure of personal IP address via Email

**Target**: Weblate

**Reported on**: hackerone

**Bug Type**: PII Exposure

**Severity**: Low

**Report URL**: https://hackerone.com/reports/3179850

## Summary
Weblate is an opensource translation integration software that translates documentations, and various commuication.
When Weblate sends an email for various reasons such as notifications, password reset, etc. They include the Public IP address of the user doing the action.
This passes through many smtp servers in the middle, storing information. Violating GDPR as Public IP is a PII.
Impact is that exposed IP can be used for various attcks and recon.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/3179850
- https://gdpr-info.eu/recitals/no-30/
- https://github.com/WeblateOrg/weblate/pull/15102
## Tags
- PII-Exposure
- privacy-violation
- sensitive-data
