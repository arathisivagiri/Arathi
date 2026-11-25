# Sort dictionary in ascending and descending order.

dic = {"bob": 23, "charlie": 36, "alice": 72, "Eric":18,}
sort_data= sorted(dic.items(), key=lambda x: x[1])
print("Dictionary in ascending order:", sort_data)
sort_data1 = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print("Dictionary in descending order:", sort_data1)
