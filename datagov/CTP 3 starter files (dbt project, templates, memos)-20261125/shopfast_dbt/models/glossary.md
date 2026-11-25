{% docs gross_revenue %}
**Gross revenue (EUR)** — total amount paid by the customer for an order, VAT included, shipping included, before refunds.
Owner: Head of Sales · Steward: Karim Benali · Status: approved (2026-11-10)
{% enddocs %}

{# TODO (Exercise 3): add the terms net_revenue, active_customer, churned_customer, order, customer #}

{% docs net_revenue %}
Revenue from orders after refunds, excluding VAT and including shipping fees.
Formula: (total_amount_eur - refunded_eur) / 1.20, rounded to 2 decimals.
Owner: Paul Girard (Head of Finance) · Steward: Karim Benali (Analytics Engineer) · Status: approved (2026-11-25)
{% enddocs %}

{% docs active_customer %}
A customer account with at least one non-cancelled order in the previous 12 months, measured as of the report date.
Owner: Paul Girard (Head of Finance) · Steward: Karim Benali (Analytics Engineer) · Status: approved (2026-11-25)
{% enddocs %}

{% docs churned_customer %}
A previously purchasing customer with no non-cancelled order in the previous 12 months, measured as of the report date.
The 12-month window is provisional and aligned with Finance's active-customer definition; business-owner approval is still needed.
Owner: Business owner (to confirm) · Steward: Karim Benali (Analytics Engineer) · Status: draft
{% enddocs %}

{% docs customer %}
A customer is one ShopFast customer account identified by customer_id; one person may have multiple accounts.
Owner: Sara Martin (Head of Sales) · Steward: Karim Benali (Analytics Engineer) · Status: draft
{% enddocs %}

{% docs order %}
A ShopFast order is a recorded purchase transaction identified by a unique order_id, including orders that are later cancelled or returned.
Owner: Sara Martin (Head of Sales) · Steward: Senior analyst · Status: draft
{% enddocs %}
