
select * from user where email = 'john-smith1992@gmail.com';

select sum(clicks) from app_usage where user_id = '2921-299-1929182';

select count(distinct(device)) from app_usage where user_id = '2921-299-1929182';

select * from transactions where sender_id = '2921-299-1929182' or recipient_id = '2921-299-1929182';

select *
from transactions
where (sender_id = '2921-299-1929182' or recipient_id = '2921-299-1929182')
and timestamp < now()
and timestamp > now() - interval '30 days'

select * from transactions where status = 'FAILED';

select count(*) as total_transaction_count, u.email
from transactions as t
inner join user as u
on t.sender_id = u.id
group by u.email
order by total_transaction_count desc;
