# Subdomain takeover of datacafe-cert.starbucks.com

**Target**: starbucks

**Reported on**: hackerone

**Bug Type**: Subdomain takeover

**Severity**: High

**Report URL**: https://hackerone.com/reports/665398

## Summary
The researcher found a subdomain owned by Starbucks - datacafe-cert.starbucks.com, having a CNAME record pointing to an unclaimed Azure web service at azurewebsites.net. This meant that the subdomain was dangling: it still pointed to an Azure app that no longer existed.
By registering the same app name on Azure (e.g., datacafe-cert.azurewebsites.net), the researcher was able to take control of the Starbucks subdomain. This allowed them to serve content under *.starbucks.com, effectively achieving a subdomain takeover 
a high-severity vulnerability due to the potential for phishing, cookie theft, or internal application abuse.

## Bounty received ($)
Unspecified

## References
https://hackerone.com/reports/665398
## Tags
- subdomain-takeover
- dns
- azure
- cloud-misconfiguration
- domain-hijacking
