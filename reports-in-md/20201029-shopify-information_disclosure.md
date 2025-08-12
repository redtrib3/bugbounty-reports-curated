# [Information Disclosure] Amazon S3 Bucket of Shopify Ping (iOS) have public access of other users image

**Target**: shopify

**Reported on**: hackerone

**Bug Type**: Information Disclosure

**Severity**: High

**Report URL**: https://hackerone.com/reports/1021906

## Summary
Shopify ping is a shopify mobile application that enables integration with an already used chat platform, allowing centralization.
The researcher found an exposed amazon s3 bucket with directory listing enabled exposing shared user images from private chats, This endpoint
was discovered when testing the chat app, and the researcher noticed that the send images where stored in an s3 bucket owned by shopify.

## Bounty received ($)
2900

## References
- https://hackerone.com/reports/1021906
## Tags
- sensitive-data-exposure
- cryptographic-failure
- misconfiguration
