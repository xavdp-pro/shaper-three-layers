# Enterprise OS Demo Company
## Office Furniture — B2B + B2C

## 0. Purpose

The demo company is intentionally small but believable.

It sells office furniture to businesses and individuals.

The demo should look like a real company that has been operating for several years.

It must contain enough historical data to support meaningful dashboards, trends, search, and natural-language questions.

---

# 1. Demo organization

Suggested small team:

- Owner / Director
- Salesperson
- Secretary / Operations Coordinator
- Purchasing / Stock Coordinator
- Support / Logistics person

This is not a universal organization chart.

It is a simple demo structure large enough to show:

- roles;
- shared mailboxes;
- task assignment;
- multiple participants;
- responsibility;
- decisions;
- communication;
- purchasing and sales.

---

# 2. Customers

Include:

- individuals;
- small businesses;
- larger business customers.

Each customer may have:

- several addresses;
- principal contact;
- secondary contacts;
- phone;
- email;
- order history;
- quotes;
- documents;
- tasks;
- conversations.

Create enough customers to support 1–3 years of believable business analytics.

---

# 3. Products

Examples:

- ergonomic chair;
- executive chair;
- sit/stand desk;
- meeting table;
- storage cabinet;
- bookshelf;
- reception desk;
- monitor arm;
- drawer unit.

Create realistic:

- purchase history;
- price changes;
- sale-price changes;
- stock changes;
- seasonal variation;
- profitable and less-profitable items.

---

# 4. Stock example

Ergonomic Chair A:

```text
2024-04-10: buy 50 @ 100
2026-08-28: buy 20 @ 120
```

Default demo depletion:

```text
FIFO
```

Selling price is independent from stock valuation and may have its own dated history.

---

# 5. Quotes

Support:

- product lines;
- quantities;
- line discount;
- global discount;
- delivery fee;
- installation fee;
- validity date;
- frozen applied prices.

Example demo request:

> “Prepare a quote for Acme Design: 12 ergonomic chairs, 6 desks, delivery included, 5% discount on chairs.”

---

# 6. Email demo environment

Each demo employee has a personal mailbox.

Shared mailboxes:

- contact@
- sales@
- support@
- purchasing@

Use a contained mail environment that can safely simulate real activity.

Populate with realistic fictional email history.

Important demo email:

**Supplier price update**

Attachment contains updated purchase prices.

The operator asks Helm to process it.

Expected result:

- identify products;
- create new dated purchase-price records;
- do not overwrite old prices;
- show margin impact;
- create trace;
- allow approval;
- index attachment in GED.

---

# 7. GED demo documents

Prepare fictional documents:

- supplier price list;
- supplier invoice;
- restaurant receipt;
- delivery note;
- customer purchase request;
- quote;
- signed contract;
- warranty document;
- support photo;
- product PDF.

All documents should be linked to believable CRM data.

---

# 8. Restaurant receipt scenario

Flow:

```text
IMAGE / PDF RECEIPT
→ INGEST
→ OCR / EXTRACTION
→ DATE / SUPPLIER / AMOUNT / TAX / CATEGORY
→ HUMAN VALIDATION IF NEEDED
→ GED
→ RAG
→ EXPENSE RECORD
→ ACCOUNTING CONNECTOR READY
```

Questions Helm can answer:

- “Find restaurant receipts from last month.”
- “How much did we spend on client meals?”
- “Show me the source documents.”

---

# 9. Customer email → invoice-by-voice scenario

Precondition:

- customer already exists;
- email already exists in mailbox;
- related order context exists.

Demo:

1. user opens / receives customer email;
2. user asks by voice:
   - “Prepare the invoice for this customer for the requested order.”
3. Helm resolves customer and order;
4. document is generated;
5. user sees preview;
6. user validates or edits;
7. decision/action is traced;
8. generated document is linked to customer and GED.

This scenario demonstrates:

- voice;
- CRM context;
- document generation;
- traceability;
- decision;
- human validation.

---

# 10. Dashboard data

Create believable 1–3 year activity.

Include variation in:

- monthly revenue;
- product mix;
- customer type;
- average order size;
- gross margin;
- purchasing cost;
- stock-outs;
- discounts;
- delivery fees.

Helm should be able to answer:

- “Which month had the highest revenue?”
- “Which product made us the most money?”
- “Which customer generated the highest margin?”
- “What changed this year?”
- “Which products are at risk of stock-out?”
- “Why was June better than May?”

---

# 11. Demo telephony

Do not provision a permanent number by default.

Explain that the telephony module supports:

- AI receptionist;
- human receptionist;
- schedules;
- call routing;
- call queues;
- softphones;
- mobile softphone;
- transcription;
- summaries;
- CRM integration;
- click-to-call.

For project-specific demonstrations, a test number may be temporarily provisioned.

---

# 12. Demo principle

The demo must feel usable even if Helm is ignored.

Without the agent, the user can operate manually.

With Helm, the same business graph becomes dramatically faster to navigate and control.

This contrast is intentional.


---

# 13. Seed-data coherence

Demo data must form one coherent fictional world.

Do not generate independent random tables.

A customer email should refer to:
- an existing customer;
- an existing contact;
- an existing order or quote;
- products that actually exist;
- prices valid at that date;
- documents available in GED when referenced.

A supplier price change should correspond to:
- a known supplier;
- real demo SKUs;
- previous purchase prices;
- later margin changes.

This coherence is what allows Helm to appear grounded rather than theatrical.

---

# 14. Demo historical timeline

Prepare a consistent 24–36 month timeline with:

- customer creation;
- quotes;
- accepted/rejected quotes;
- orders;
- deliveries;
- supplier purchases;
- stock lots;
- price changes;
- discounts;
- support events;
- expenses;
- decisions;
- emails;
- documents.

The objective is meaningful analytics, not large data volume.

---

# 15. Demo success criterion

The visitor should leave with four convictions:

1. **The company already works manually.**
2. **Helm understands the same connected operational reality.**
3. **Delegation can be progressive and controlled.**
4. **The system can prove what happened and recover from controlled change.**

A useful internal milestone for the demo architecture is:

> **A simulated month of operations can run without unexplained state, with decisions and important actions traceable end-to-end.**
