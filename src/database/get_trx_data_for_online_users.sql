with trx as ( 
select id, created_at, merchant_id, amount  from accept_transactions 
where gateway_type in ('VPC', 'MIGS') and integration_type in ('online', 'moto') and  success = TRUE
and is_live_integration = TRUE
AND is_refund = FALSE AND is_void = FALSE AND is_voided = FALSE AND is_auth = false
), 
billing as ( select phone_number, transaction_id, email from payment_methods_billingdata ),

card as (select card_number_masked, card_bin, transaction_id, card_hash, card_number_hash
from payment_methods_transactionrisk ), 

merchant_det as (select distinct merchant_id, merchant_name, company_name
from accept_transactions),

pre_merchant_det as (

select card_number_hash, phone_number , merchant_id , email, count(*) as trx, 
sum(amount) as total_spent, min(created_at) as first_trx_date, max(created_at) as last_trx_date
from trx t 
left join billing b on t.id = b.transaction_id
left join card c on t.id = c.transaction_id
group by card_number_hash, phone_number , merchant_id , email  ) 


select * from pre_merchant_det pm 
inner join merchant_det md on md.merchant_id = pm.merchant_id
