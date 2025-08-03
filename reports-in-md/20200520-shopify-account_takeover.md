# Takeover an account that doesn't have a Shopify ID and more

**Target**: Shopify

**Reported on**: hackerone

**Bug Type**: Account Takeover

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/867513

## Summary
In a Shopify account (an account to manage a store), there is a concept called PoS (Point of Sale) where we can create a channel for a physical store. New staff accounts are created for staff in the physical store.

**Shopify store** - An account for a business  
**Shopify ID** - An account in the Shopify platform.  
(You can create Shopify stores without needing a Shopify ID!)  
**Dev store** - A free development store used for testing purposes.

**PoC**:  
1. Create a dev store in Shopify  
2. Intercept the request and change the email to attacker email.  
3. Install POS in the dev store.  
4. Add a new staff profile, intercept and change the email to the victim's (the account you want to takeover)  
5. Refresh the page — Shopify offers to "Create a Shopify ID for victim@shopify.com"  
6. Shopify creates a Shopify ID for the victim's email without verification.

## Bounty received ($)
22500

## References
- https://hackerone.com/reports/867513
- https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/AyPRNnVzskrRrPfNPhDbvnq1?response-content-disposition=attachment%3B%20filename%3D%22Takeover.mp4%22
- https://docs.shopify.com
## Tags
- account-takeover
- identity-spoofing
- improper-access-control
