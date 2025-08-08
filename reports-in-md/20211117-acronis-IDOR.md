# IDOR vulnerability (Price manipulation)

**Target**: Acronis

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: Medium

**Report URL**: https://hackerone.com/reports/1403176

## Summary
The researcher found a IDOR vulnerability in payment processing that will lead to price manipulation i.e the increase and decrease of price in a marketplace.
To reproduce the bug, go to the the website (acronis.cz), buy any product go to cart and click on buy now, intercept the request and change the price and forward the request.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/1403176
## Tags
- IDOR
