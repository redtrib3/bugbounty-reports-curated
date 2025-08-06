# Insecure Direct Object Reference (IDOR) Allows Viewing Private Report Details via /bugs.json endpoint

**Target**: hackerone

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/2487889

## Summary
A researcher found a vulnerable endpoint - bugs.json in hackerone.com which can reveal private bug reports. The endpoint had two required POST parameters - text_query, organization_id
the text_query requires a single number such as `1`. This will query all reports containing that digit. The organization_id can be found from the organization's page.
This request dumped details about a private report such as - `title,url,id,state,substate,severity_rating,readable_substate,created_at,submitted_at,reporter_name`

The researcher later during the triage also found the parameters `limit` and `page` which can be used to point out a report faster without having to guess with the `text_query` parameter.
the reseacher also mentions that the parameter `substates%5B%5D=editing` can be added to the request to disclose drafted reports.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/2487889
## Tags
- IDOR
- sensitive-data
