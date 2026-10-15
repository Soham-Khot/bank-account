| Bancaccount : |
Class Attributes : | bank_name | balance | total_accounts | 
Instance Attributes : | owner | transaction |
Constructor : | __init__ |

Instance Methods : | deposit | withdraw | summary | transfer_to |
1.deposit : use for handle deposit operations on perticuler objects
2.withdraw : use for handle withdraw operations on perticuler objects
3.summary : use for show account owner and balance
4.transfer_to : use for transfer amount from one account to another 

Static Methods : | validate_amount | is_valid_owner | format_money |
1.validate_amount : use for checking whether give amount is number or not and it is static because this is not related to any object or class , just for validation 
2.is_valid_owner : use for checking whether give owner name is contains only characters and length is greater than 2 and it is static because this is not related to any object or class , just for validation
3.format_money : use for formating amount like this (12,500.00) so just taking one int as input and return formating string 