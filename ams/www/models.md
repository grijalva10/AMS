# Current Tools

- weebly.com - website, dns
- gsuite - email, word processing, spreadsheet
- jotform.com - quote forms, service request forms
- epaypolicy.com - payment processing, transaction receipts
- esignatures.io - payment information collection, proposals (quotes)
- closecrm.com - customer relationship management
- slack.com - team communication
- dochub - policy application contract
- aws - cloud infrastructure

# Models

- Insurance Agency
- Agent
- Policy
- Policy Type
- Claim
- Insured
- Payment Request

# Service Requests

- Certificate Request
- Report A Claim
- Make A Payment
- No Loss Warranty
- Policy Change
- ProfitLoss
- Broker of Record
- Resume

# Carrier Payment Process

In order to streamline and standardize payments to carriers and policy binding, the following process will be adopted effective 06/01/2023.

## When binding a policy with a direct bill carrier

The broker will collect the insured's credit card info and 2 transactions will be processed:
1. Broker will process a payment for their broker fee only using [https://b.link/jmgpay](https://b.link/jmgpay)
2. Broker will use the insured's credit card info to make a down payment directly with the carrier and bind the policy.

## When binding a policy with an agency bill carrier

The broker will collect the insured's credit card info and 1 transaction will be processed.
- Broker will process a payment for the policy down payment plus broker fee using [https://b.link/jmgpay](https://b.link/jmgpay)
- Broker will submit a payment request to customer service using [https://b.link/payrequest](https://b.link/payrequest) (this request will reflect in Slack)
- Customer service team will make the payment as requested and confirm completion with the broker.

### Notes

- If the payment is required to bind, please advise customer service.
- If the payment request is a rush, please advise customer service.
- Please set proper expectations with your client, not every instance can be a rush.
- Instructions for how to pay each carrier are available [here](#).

| Carrier       | How to Quote             | How to Collect $$$        | How to send App         | How to Pay Carrier                  |
|---------------|--------------------------|---------------------------|-------------------------|-------------------------------------|
| ISC           | ISC E-Sign Docs          | Broker Collects All Money | ISC Docusign            | Payment Request (only if balance due) |
| HCC           | JMG Quote + Carrier App  | Collect Broker Fee Only   | Dochub                  | Clients Card                        |
| BTIS          | JMG Quote + Carrier App  | Broker Collects All Money | Dochub                  | Payment Request                     |
| Shield        | JMG Quote + Carrier App  | Broker Collects All Money | Dochub                  | Payment Request                     |
| Pathpoint     | JMG Quote + Carrier App  | Broker Collects All Money | Dochub                  | TBD                                 |
| NCCI          | JMG Quote + Carrier App  | Collect Broker Fee Only   | Dochub                  | Clients Card                        |
| Texas Mutual  | JMG Quote                | Broker Collects All Money | N/A                     | Payment Request                     |
| NJCRIB        | JMG Quote                | Broker Collects All Money | N/A                     | Payment Request                     |
| Biberk        | JMG Quote                | Collect Broker Fee Only   | N/A                     | Clients Card                        |
| PIE           | JMG Quote                | Collect Broker Fee Only   | Dochub                  | Clients Card                        |
| Bolt          | JMG Quote + Carrier App  | Collect Broker Fee Only   | Dochub                  | Supply Clients Info to Bolt for Payment |
| Next          | JMG Quote                | Collect Broker Fee Only   | N/A                     | Clients Card                        |
| Coterie       | JMG Quote                | Collect Broker Fee Only   | N/A                     | Clients Card                        |
| Bonds Express | JMG Quote                | Collect Broker Fee Only   | Dochub                  | Clients Card                        |
| Simple Bonds  | JMG Quote                | Broker Collects All Money | Dochub                  | Payment Request                     |
| Appalachian   | JMG Quote + Carrier App  | Broker Collects All Money | Dochub                  | Payment Request                     |
| NCRB          | JMG Quote + Carrier App  | Broker Collects All Money | Dochub                  | Payment Request                     |
| Pouch         | JMG Quote                | Collect Broker Fee Only   | N/A                     | Clients Card                        |

## Table Notes

- carrier apps - internal carrier rating engine and quote generation, sales invoices
- JMG Quote - jotforms and cognito forms
- Broker Collects All Money - agency bill carrier
- Collect Broker Fee Only - direct bill carrier

- leads are managed in close crm
- Agent generates a quote from carrier or MGA

If the MGA is ISC the following steps occur:

- internal ISC process

If the MGA or Carrier requires Prepayment for a policy:

- The Agent requests bind using Carrier or MGA platform.
- The Policy is bound pending payment to carrier or MGA.
- The Agent downloads the policy invoice.
- The Agent fills out the 'Payment Request' form at [https://form.jotform.com/231441110348039](https://form.jotform.com/231441110348039).
- The 'Payment Request' form has the following inputs: Broker, Payee (Carrier), Policy or App Number, Type of Policy, Business Name, Insured, Contact Name, Insured, Email, Insured, Amount to Pay, Amount Collected, Invoice
- The Service Agent pays the Carrier or MGA.
- The Agent checks with the Carrier or MGA platform to see if the policy is bound

If the MGA or Carrier doesn't require Prepayment for a policy:

- Agent fills out a form which creates a URL of a 'Contract' with [https://esignatures.io](https://esignatures.io)
- The URL of the 'Contract' contains the policy quote information, financials and allows the lead to submit credit card payment information, a name and a phone number
- The lead fills out 'Contract' form, submit forms and a PDF link is generated with the payment info, name, phone, company name (optional). The resulting data is posted in a Slack channel called #contract-signed
- The agent monitors #contract-signed, clicks the esignatures.io executed PDF contract to extract payment information.
- Agent goes to [https://jmgia.epaypolicy.com/](https://jmgia.epaypolicy.com/) and enters payment information which is built with [https://epaypolicy.com/](https://epaypolicy.com/)
- epaypolicy.com processes the payment and outputs a 'Transaction'
- The 'Transaction' data is posted in the Slack channel #payments and creates a row in a Google Sheets document.
- If the carrier or MGA requires payment first a 'Payment Request' form in filled out at [https://form.jotform.com/231441110348039](https://form.jotform.com/231441110348039).
- The 'Payment Request' form has the following inputs: Broker, Payee (Carrier), Policy or App Number, Type of Policy, Business Name, Insured, Contact Name, Insured, Email, Insured, Amount to Pay, Amount Collected, Invoice
- The service agents monitor the Google Sheets documents with transaction from epaypolicy.com.
