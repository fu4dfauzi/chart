

#number of cash to credits is altered in 
# http://127.0.0.1:8000/admin/billing/credittocash/
# 700 - $50
# 250 - $20
# 100 - $10

#number of credit deducted per message
msgcredit = 50
#number of credits to start off with
creditstart = 500
#number of credits to add teacher/student places an order
orderadd = 20

feat_days_choices = (
	('400',  '3 days for 400 credits'),
	('800',  '7 days for 800 credits'),
	('1600',  '14 days for 1600 credits')
)
feat_days_choices_dict = {
'400':3,
'800':7, 
'1600':14
}


img_days_choices = (
	('100',  '30 days for 100 credits'),
	('300',  '90 days for 300 credits'),
	('500',  '365 days for 500 credits')
)
img_days_choices_dict = {
'100':30,
'300':90, 
'500':365
}


ana_days_choices = (
	('40',  '30 days for 40 credits'),
	('120',  '90 days for 120 credits'),
	('200',  '365 days for 200 credits')
)
ana_days_choices_dict = {
'40':30,
'120':90, 
'200':365
}


studentbi_days_choices = (
	('100',  '30 days for 100 credits'),
	('300',  '90 days for 300 credits'),
	('500',  '365 days for 500 credits')
)
studentbi_days_dict = {
'100':30,
'300':90, 
'500':365
}