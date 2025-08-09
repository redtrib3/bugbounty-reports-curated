# IDOR able to buy a plan with lesser fee

**Target**: Automattic

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: Informative

**Report URL**: https://hackerone.com/reports/1679276

## Summary
The researcher found a vulnerablity that let's a user pay for an order with the same amount but different currency. in the url - https://account.mailpoet.com/orders/new?p=214&cur=usd
change the `cur` parameter to any other currency and it shows the same amount, The security team triaged this as informative, as the platform has same price for every product in every currency by design.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/1679276
## Tags
- IDOR
