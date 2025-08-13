# Subdomain Takeover Via via Dangling NS records on Amazon Route 53 http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io

**Target**: Kubernetes

**Reported on**: hackerone

**Bug Type**: Subdomain takeover

**Severity**: Medium

**Report URL**: https://hackerone.com/reports/746000

## Summary
The researcher found out that a subdomain owned by k8s.io (kubernetes) - http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io is pointed via Name Server records to AWS route 53.
These name server records have been deleted, and researcher was able to create a matching zone file, and takeover full control of the domain, and all DNS records.

## Bounty received ($)
250

## References
- https://hackerone.com/reports/746000
## Tags
- subdomain-takeover
