SELECT customer_id, first_name, last_name, email, phone
	FROM public.customer;
	
	
	SELECT *
FROM public.customer
WHERE last_name = 'Smith';


	SELECT *
FROM public.customer
WHERE last_name = 'Jones';

	SELECT *
FROM public.customer
WHERE first_name != 'Scott';