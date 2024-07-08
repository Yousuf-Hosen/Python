import pandas as pd
mydata={
    "Days" :["saterday","sunday","monday","tuesday","wednesday","Thusday","Friday"],
    "calories" : [420,233,877,98,65,78,88],
    "duration":[50,53,23,45,98,67,44]
}
val=pd.DataFrame(mydata)
print(val)
""" 
একটি পান্ডাস ডেটাফ্রেম হল একটি 2 মাত্রিক ডেটা স্ট্রাকচার, যেমন একটি 2 ডাইমেনশনাল অ্যারে, বা সারি এবং কলাম সহ একটি টেবিল।
পান্ডারা locএক বা একাধিক নির্দিষ্ট সারি (গুলি) ফেরত দিতে অ্যাট্রিবিউট ব্যবহার করে
 """
print(val.loc[0])
print(val.loc[3])
print(val.loc[5])

