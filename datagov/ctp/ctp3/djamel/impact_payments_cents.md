A switch from euros to cents makes every payment amount 100 times too large.
This affects stg_payments.amount, fct_orders.refunded_eur, and fct_orders.net_revenue_eur.
Downstream impacts include dim_customers, the Sales dashboard, the Finance report, and the churn-prediction model.
Alert the Finance owner (Paul Girard), the Sales owner (Sara Martin), and the data steward before deployment.
Block the batch until EUR range and distribution tests pass, and Finance approves any unit change.
