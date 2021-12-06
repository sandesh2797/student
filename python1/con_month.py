print('jan'    'feb'    'march'    'apr'   'may'   'jun'   'july' '  aug'   'sep'   'oct' 'nov' 'dec')

month=(input("enter the month   "))


if month in ('feb'):
    print("28/29")
elif month in  ('jan' 'march' 'apr' 'may'):
    print('30')
elif month in ('jun' 'july' 'aug' 'sep' 'oct' 'nov' 'dec'):
    print('31') 

else:
    print("enter correct month ")           