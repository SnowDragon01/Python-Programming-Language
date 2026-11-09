# 	• एक फंक्शन sum_list(numbers) बनाएं जो इनपुट के रूप में नंबरों की एक लिस्ट (जैसे [1, 2, 3, 4]) ले और उसके सभी तत्वों (elements) का कुल योग (sum) रिटर्न करे।

def sum_list(user_list):
    sum=0
    for elements in range(0,len(user_list),1):
        sum+=user_list[elements]
    print(sum)

prime=[2,3,5,7,11,13,17,19,23]

sum_list(prime)
