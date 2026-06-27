# Search faster in Classic Outlook

Status: Production draft

## High-level overview
Use this one-page cheat sheet when you need to find mail in Classic Outlook for Windows with a work account. Start with the Search box, choose the right scope, then add one useful term at a time.

## Architectural diagram concepts
Search has two parts: **scope** controls where Outlook looks, and **terms** control what Outlook returns. The Word asset uses an accessible shaded scope panel and a three-column table for fast scanning.

## Step-by-step setup
1. Select the Search box, or press **Ctrl+E**.
2. Check the search scope before you type.
3. Type the most specific word, name, subject, or phrase you know.
4. Add one supported search expression when useful.
5. Press **Enter**.
6. Clear the search when finished so your normal message list returns.

## Common search terms
| Need | Enter | Note |
| --- | --- | --- |
| From a person | `from:"Jordan White"` | Use the sender name or address. |
| Sent to a person | `to:"Jordan White"` | Use when you know a recipient. |
| Copied to a person | `cc:"Jordan White"` | Use when the person was copied. |
| Subject phrase | `subject:"renewal proposal"` | Best when the subject is known. |
| Exact phrase anywhere | `"effective date"` | Keeps the words together. |
| Has an attachment | `hasattachments:yes` | Finds messages with files. |
| Does not have an attachment | `hasattachments:no` | May vary by tenant; review results. |
| Unread messages | `isread:no` | Use with another term when possible. |
| Read messages | `isread:yes` | Use with another term when possible. |
| Category | `category:"Waiting"` | Category names must match your mailbox. |
| Received on a date | `received:06/15/2026` | Use your tenant-supported date format. |
| Sent on a date | `sent:06/15/2026` | Use your tenant-supported date format. |
| Important message | `importance:high` | Matches high importance mail. |
| File name or extension | `attachment:xlsx` | Pair with `hasattachments:yes`. |
| Body word | `body:renewal` | Use when the word is not in the subject. |

## Useful combinations
| Goal | Search expression | Why it helps |
| --- | --- | --- |
| Renewal from Jordan | `from:"Jordan White" renewal` | Combines person and topic. |
| Jordan renewal with a file | `from:"Jordan White" renewal hasattachments:yes` | Narrows a long thread list. |
| Unread Waiting category | `isread:no category:"Waiting"` | Finds pending categorized mail. |
| Excel attachments | `hasattachments:yes attachment:xlsx` | Finds messages with Excel files. |
| Exact subject | `subject:"Q3 renewal review"` | Best for a known subject line. |

## Scope panel
| Scope | Searches | Use when |
| --- | --- | --- |
| Current Folder | Only the open folder | You know the folder. |
| Subfolders | The folder and folders beneath it | You know the area, not the exact folder. |
| Current Mailbox | The selected mailbox | You know the mailbox. |
| All Mailboxes | Available mailboxes in your profile | You do not know where the message is. |
| All Outlook Items | Mail and other Outlook items | You may need calendar or task items too. |

## Search a shared mailbox
1. Open a folder inside the shared mailbox.
2. Select the Search box.
3. Set the scope to the current folder or shared mailbox when available.
4. Enter your terms.
5. Confirm the result location before acting.

## Common Gotchas
- Do not assume no result means the message was deleted.
- Do not search all mailboxes when one folder is enough.
- Do not leave an old search active while reviewing new email.
- Search results can depend on mailbox access, indexing, cache, and tenant settings.
- Ask for help at [[APPROVED SUPPORT PATH REQUIRED]] if search repeatedly fails.

## Footer text
Take Control of Your Inbox | Classic Outlook search cheat sheet | [[LAST REVIEWED DATE REQUIRED]]
