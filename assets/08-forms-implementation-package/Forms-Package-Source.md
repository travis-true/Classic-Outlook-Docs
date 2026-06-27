# Feedback forms implementation package source

Status: Production draft

This package gives implementers specifications for two Microsoft Forms and one SharePoint tracking list. It does not deploy Microsoft Forms or SharePoint, create live links, or imply approval.

## High-level overview

Create two employee-facing feedback paths for the Take Control of Your Inbox resources:

1. **Guide feedback** helps IT Training & Enablement learn whether Outlook resources are useful, clear, and easy to apply.
2. **Report outdated instructions** helps employees flag steps, screenshots, links, or videos that no longer match Outlook or company process.

Both forms must warn employees not to include customer, member, employee, account, claim, policy, medical, financial, or other sensitive information.

## Architectural diagram concepts

Employee opens resource → selects descriptive link → completes Microsoft Form → response is reviewed by IT Training & Enablement → accepted item is logged in SharePoint tracking list → owner validates, updates, and closes item.

## Step-by-step setup

1. Confirm the approved support, training, SharePoint, feedback, outdated-instructions, privacy, and publication paths.
2. Build the Guide feedback form from the field schema.
3. Build the Report outdated instructions form from the field schema.
4. Configure employee-only response settings unless an approved exception exists.
5. Add confirmation messages.
6. Create the SharePoint tracking list.
7. Connect response review workflow manually or with approved automation.
8. Test desktop, browser, keyboard, screen reader, and mobile behavior.
9. Add approved descriptive links to related resources.
10. Complete privacy, accessibility, security, and publication reviews.

## Common gotchas

- Do not request sensitive information in open text fields.
- Do not enable file upload until the storage location and review process are approved.
- Do not publish links until approval is recorded.
- Do not use color alone for status or severity.
- Do not treat these specifications as a deployed form.

## Standard placeholders

[[APPROVED SUPPORT PATH REQUIRED]]
[[APPROVED TRAINING CONTACT REQUIRED]]
[[APPROVED SHAREPOINT RESOURCE LINK REQUIRED]]
[[APPROVED FEEDBACK LINK REQUIRED]]
[[APPROVED OUTDATED-INSTRUCTIONS LINK REQUIRED]]
[[APPROVED POLICY LINK REQUIRED]]
[[LAST REVIEWED DATE REQUIRED]]
[[NEXT REVIEW DATE REQUIRED]]
[[TARGET RESPONSE TIME REQUIRED]]
[[PUBLICATION APPROVAL REQUIRED]]
