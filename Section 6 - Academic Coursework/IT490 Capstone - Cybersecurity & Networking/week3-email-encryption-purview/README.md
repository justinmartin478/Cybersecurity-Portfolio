# Host-to-Host Email Encryption with Microsoft Purview

*Scenario based implementation plan for protecting HIPAA and payroll information sent from HR to the CIO and an external health insurance provider*

**Course:** IT490 Capstone - Cybersecurity & Networking &nbsp;·&nbsp; **Week:** 3 &nbsp;·&nbsp; **Type:** Report

> The full assignment is rendered below. The original and a formal copy are available for download: [**Word document**](./IT490_Week3_Host_to_Host_Email_Encryption_Portfolio_Justin_Martin.docx) · [**PDF**](./IT490_Week3_Host_to_Host_Email_Encryption_Portfolio_Justin_Martin.pdf)

| Implementation Steps | Mail Flow Rules | Acceptance Tests | Protection Template |
| --- | --- | --- | --- |
| 10 | 2 | 8 | DNF |

---

## Summary

As ABC's systems administrator, I would configure Microsoft Purview Message Encryption so Human Resources can send sensitive information to the internal CIO and an external health insurance provider. I would combine automatic mail flow rules with a clear Outlook workflow so encryption does not depend only on someone remembering to select it.

This report explains a proposed configuration. It does not claim that an ABC tenant was configured or that the validation tests were performed.

## Project Snapshot

|  |  |
| --- | --- |
| **Author** | Justin Martin |
| **Course** | IT490 Capstone, Green River College |
| **Date** | October 7, 2026 |
| **Platform** | Microsoft 365 (Exchange Online, Microsoft Purview Message Encryption, Azure Rights Management) |
| **Skills demonstrated** | Rights Management activation, Exchange Online PowerShell, mail flow rule design, forced-TLS partner connectors, HIPAA-aware data handling, acceptance test planning |

## 01. Scenario and Recommended Approach

Purview uses Azure Rights Management to combine encryption with identity and access controls. It supports messages sent inside and outside the organization. In this scenario, host to host means protected email between the HR user and the intended recipient through Microsoft 365. It does not require a direct tunnel between their computers (Microsoft, n.d.g).

**Figure 1 — Planned protected message flow for HR, the CIO, and the insurance provider**

![Message flow diagram in which the HR sender on the ABC LAN sends through Exchange Online, where mail flow rules apply Do Not Forward encryption, and the protected message goes back to the CIO on the LAN or out to the insurance provider over a forced-TLS connector](./screenshots/figure-1-protected-message-flow.png)

| Role | Illustrative address | Access location |
| --- | --- | --- |
| HR sender | hr@abc.example | ABC LAN |
| CIO | cio@abc.example | ABC LAN |
| Insurance provider | benefits@healthprovider.example | Outside ABC LAN |

All addresses are fictional placeholders. The implementation would substitute ABC's verified accounts and the provider's approved recipient. LAN location alone would not grant permission to read a protected message.

### 1. Confirm prerequisites

I would confirm that HR and the CIO have eligible licenses, such as Office 365 E3 or Microsoft 365 Business Premium, and that their mailboxes use Exchange Online. Users benefiting from the encryption service must be appropriately licensed (Microsoft, n.d.f).

I would obtain only the administrative roles needed for the configuration, verify the provider's identity through an established business contact, and use fictitious records for the pilot. If ABC already uses Active Directory Rights Management Services, I would plan its migration before activating Azure Rights Management (Microsoft, n.d.k).

### Protection Choice

I would use Do Not Forward for this workflow. It adds restrictions to encrypted content, including forwarding, copying, and printing in supported experiences. These restrictions do not prevent a recipient from photographing a screen. ABC still needs trustworthy recipients and secure devices (Microsoft, n.d.g).

## 02. Enable and Verify the Encryption Service

### 2. Confirm Azure Rights Management

From a supported Windows PowerShell administrative workstation, I would install the AIPService module and sign in with an authorized account. Most eligible tenants already have the service enabled. Activation must now be performed through PowerShell rather than an admin portal (Microsoft, n.d.a).

**Windows PowerShell**

```powershell
Install-Module AIPService -Scope CurrentUser
Import-Module AIPService
Connect-AipService
Get-AipService
```

If the returned status is Enabled, I would continue. If it is Disabled, after verifying the prerequisites and absence of an unresolved AD RMS deployment, I would run the following and check the status again:

**Windows PowerShell**

```powershell
Enable-AipService
Get-AipService
```

### 3. Check Exchange Online configuration

In an Exchange Online PowerShell session, I would connect with the account authorized to manage the relevant settings:

**Exchange Online PowerShell**

```powershell
Install-Module ExchangeOnlineManagement -Scope CurrentUser
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@abc.example
Get-IRMConfiguration
```

AzureRMSLicensingEnabled should be True. If it is False, I would enable it and recheck the configuration (Microsoft, n.d.k):

**Exchange Online PowerShell**

```powershell
Set-IRMConfiguration -AzureRMSLicensingEnabled $true
Get-IRMConfiguration
```

### 4. Run an internal configuration test

**Exchange Online PowerShell**

```powershell
Test-IRMConfiguration -Sender hr@abc.example `
    -Recipient cio@abc.example
```

The two addresses must be real users in ABC's tenant. I would review the output for successful template acquisition, encryption, and decryption. A failure would be investigated before deployment. This cmdlet checks service configuration; it does not replace a real delivery test to the insurance provider (Microsoft, n.d.k).

For this plan, I would retain Microsoft's default management of the tenant root key. ABC would evaluate a different key management arrangement only if its requirements called for it (Microsoft, n.d.k).

## 03. Configure Automatic Protection

### 5. Create the HR mail flow rules

Before building the external rule, I would create a mail contact for the provider's approved address under Recipients > Contacts in the Exchange admin center. The "recipient is" condition only matches mailboxes, mail users, and mail contacts that exist in ABC's directory, so without the contact the insurer could not be selected in the rule (Microsoft, n.d.e).

In the Microsoft 365 admin center, I would open Admin centers > Exchange, then Mail flow > Rules > Create a new rule. I would create the two rules below. Within each rule, all listed conditions must match (Microsoft, n.d.b).

| Setting | Internal rule | External rule |
| --- | --- | --- |
| Name | ABC HR to CIO protection | ABC HR to insurer protection |
| Sender location | Inside the organization | Inside the organization |
| Sender | hr@abc.example | hr@abc.example |
| Recipient | cio@abc.example | benefits@healthprovider.example (mail contact) |
| Action | Apply encryption and rights protection | Apply encryption and rights protection |
| Template | Do Not Forward | Do Not Forward |

For the action, I would select Modify the message security > Apply Office 365 Message Encryption and rights protection, then choose Do Not Forward. If the template list is empty, I would return to the service checks rather than saving an incomplete rule (Microsoft, n.d.b).

### 6. Review and enable the rules

I would review the conditions, place the rules where existing rules cannot bypass them, select Enforce, save, and enable them. The initial rollout would use the approved pilot mailbox and test recipients. After validation, I would expand the sender scope to all authorized HR accounts and document the approved recipient list.

The CIO rule intentionally includes an internal recipient. A condition requiring every recipient to be outside ABC would leave that part of the assignment uncovered. I would also configure a corresponding CIO to HR rule if new messages from the CIO need automatic protection.

### Transport Security to the Provider

Purview protects the message content, but I would also lock down the server-to-server hop to the insurer. Exchange Online uses opportunistic TLS by default, which can fall back to an unencrypted connection if the other side does not offer TLS (Microsoft, n.d.d). Under Mail flow > Connectors, I would create a connector from Office 365 to a partner organization, scope it to the provider's domain, and select Always use Transport Layer Security (TLS) to secure the connection. Mail that cannot meet that requirement would be rejected instead of sent in the clear (Microsoft, n.d.j). I would confirm the provider supports TLS before enabling the connector so benefits mail does not start bouncing.

### Scope and Handling Exceptions

These rules protect the specified communication paths. They do not authorize other recipients or protect every possible HR destination. HR must use manual protection for other approved sensitive messages, and ABC should evaluate broader destination controls and data loss prevention policies for its actual environment.

ABC cannot use an outbound encryption rule to protect a new message arriving from an outside sender. The provider should reply within the protected conversation or use its own approved secure sending process (Microsoft, n.d.b).

## 04. Send and Receive an Example Message

### 7. Compose the message in Outlook

In Outlook on the web, HR would create a new message, verify the intended address, and use a neutral subject. Under Options > Encrypt, HR would select Do Not Forward, confirm the protection notice, attach the approved file, and send. The automatic rule also protects matching messages if HR forgets the manual selection (Microsoft, n.d.i).

| Field | Fictional external example |
| --- | --- |
| From | hr@abc.example |
| To | benefits@healthprovider.example |
| Subject | ABC benefits review request |
| Protection | Do Not Forward |
| Attachment | Benefits_Test_Record.docx |
| Body | Hello, please review the attached fictional benefits record for employee TEST001 and confirm receipt by replying within this protected message. Thank you, ABC Human Resources. |

For the CIO, I would send a separate protected message to cio@abc.example with a fictional payroll review file, Payroll_Test_Summary.xlsx. Separate messages let HR tailor the information to each recipient's business need instead of sharing the same records with everyone.

### 8. Open and reply securely

The CIO would sign in to the intended ABC account and open the protected message in supported Outlook. The provider's experience depends on its email service and client. It may open the message directly in supported Outlook or follow the secure message link and authenticate in the browser. Where available, a passcode may be delivered to the recipient mailbox (Microsoft, n.d.h).

Both recipients should reply within the protected experience so the response retains protection. If the provider cannot open the message, HR should contact IT instead of resending sensitive content without encryption (Microsoft, n.d.h).

### Attachment Precautions

Supported Word and Excel attachments can inherit rights protection. I would validate the chosen format before exchanging real records. I would not assume that every file format has persistent protection after download. A SharePoint or OneDrive link requires its own access permissions; encrypting the email does not automatically protect the linked file (Microsoft, n.d.f).

## 05. Validation and Operational Safeguards

### 9. Test before releasing real information

The following checks are expected acceptance criteria, not observed results. I would retain the actual test evidence with the change record, using fictitious content and limiting access to administrative records.

| Test | Expected result |
| --- | --- |
| HR to CIO | The CIO can open the message using the intended ABC account. |
| HR to external provider | The approved provider can authenticate and read the message. |
| Automatic enforcement | A matching test message sent without manual encryption is protected by the rule. |
| Unauthorized account | A different test account cannot open the protected content. |
| Recipient restrictions | Forwarding, copying, and printing restrictions work in the tested client. |
| Protected reply | HR can read the recipient's reply through the protected conversation. |
| Attachment access | The approved recipient can open the test attachment; an unauthorized test account cannot. |
| Rule boundaries | A harmless message outside the defined sender or recipient scope does not unexpectedly match. |

I would inspect message trace for delivery, review the effective rule settings, and confirm recipient access directly. Successful delivery alone would not prove that protection was applied. Any failure would keep real PHI and payroll data out of the workflow until resolved.

### 10. Maintain secure daily use

I would train HR to verify recipients, avoid sensitive subject lines, send only necessary records, and report access problems. I would pair encryption with MFA, device security, mailbox access reviews, and the organization's retention and audit procedures.

Health information may be PHI depending on ABC's role and the context; payroll information is sensitive but is not automatically PHI. Where HIPAA applies, ABC must evaluate its obligations and applicable business associate agreements. Microsoft's services and agreements can support compliance, but encryption alone does not establish it (Microsoft, n.d.c).

### What I Learned

The main lesson is that an internal recipient still needs protection. I would apply the policy based on the sender, recipient, and sensitivity of the information, then verify that the intended person can actually use the protected message.

## References

Microsoft. (n.d.a). *Activate the Azure Rights Management service*. Microsoft Learn. https://learn.microsoft.com/en-us/purview/activate-rights-management-service

Microsoft. (n.d.b). *Define mail flow rules to encrypt email messages*. Microsoft Learn. https://learn.microsoft.com/en-us/purview/define-mail-flow-rules-to-encrypt-email

Microsoft. (n.d.c). *Health Insurance Portability and Accountability Act (HIPAA) & Health Information Technology for Economic and Clinical Health (HITECH) Act*. Microsoft Learn. https://learn.microsoft.com/en-us/compliance/regulatory/offering-hipaa-hitech

Microsoft. (n.d.d). *How Exchange Online uses TLS to secure email connections*. Microsoft Learn. https://learn.microsoft.com/en-us/purview/exchange-online-uses-tls-to-secure-email-connections

Microsoft. (n.d.e). *Mail flow rule conditions and exceptions (predicates) in Exchange Online*. Microsoft Learn. https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/conditions-and-exceptions

Microsoft. (n.d.f). *Message Encryption FAQ*. Microsoft Learn. https://learn.microsoft.com/en-us/purview/ome-faq

Microsoft. (n.d.g). *Microsoft Purview Message Encryption*. Microsoft Learn. https://learn.microsoft.com/en-us/purview/ome

Microsoft. (n.d.h). *Open encrypted and protected messages*. Microsoft Support. https://support.microsoft.com/en-us/outlook/mail/open-encrypted-and-protected-messages

Microsoft. (n.d.i). *Send S/MIME or Microsoft Purview encrypted emails in Outlook*. Microsoft Support. https://support.microsoft.com/en-us/outlook/mail/send-s-mime-or-microsoft-purview-encrypted-emails-in-outlook

Microsoft. (n.d.j). *Set up connectors for secure mail flow with a partner organization*. Microsoft Learn. https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/set-up-connectors-for-secure-mail-flow-with-a-partner

Microsoft. (n.d.k). *Set up Microsoft Purview Message Encryption*. Microsoft Learn. https://learn.microsoft.com/en-us/purview/set-up-new-message-encryption-capabilities

Documentation reviewed October 7, 2026. Microsoft may change portal wording or licensing requirements, so I would confirm both during implementation.

## Outcome

I planned a Microsoft Purview Message Encryption rollout that protects HR mail to an internal CIO and an external insurance provider with the Do Not Forward template. I wrote the PowerShell checks for Azure Rights Management and Exchange Online, designed two mail flow rules, and added a forced-TLS connector for the provider. I also defined eight acceptance tests and kept the report clear that they are expected results, not observed ones.
