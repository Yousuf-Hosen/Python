import pandas as pd
pd.options.display.max_rows=999
# defines row number by user 
val=pd.read_csv('data.csv')
print(val.to_string())
print(pd.options.display.max_rows)
""" 
আমার সিস্টেমে সংখ্যাটি 60, যার মানে যদি ডেটাফ্রেমে 60টির বেশি সারি থাকে তবে print(df)বিবৃতিটি শুধুমাত্র শিরোনাম এবং প্রথম এবং শেষ 5টি সারি প্রদান করবে।
 """
