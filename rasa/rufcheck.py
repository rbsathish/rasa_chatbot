
dic = [{'recipient_id': 'default', 'text': 'Available Biriyani '}, {'recipient_id': 'default', 'text': ' vegbiriyani:\n\t Special_Paneer_Biryani '}, {'recipient_id': 'default', 'text': ' nonvegbiriyani: \n\t egg_biriyani \n\t Chicken_Bone_Less_Pulao \n\t Keema_Biryani'}, {'recipient_id': 'default', 'text': 'choosee your biriyani from the above menu'}]
d =dict(dic)
# dict_values
# print (d)
for response in dic:
    print("Robo: ",response["text"])
# for item in dic:
#     # print(item)
#     for ftext in item.items():
#         # print(ftext)
#         # print(str(ftext))
#         d= dict(ftext)
#         print(d)
#         for v in ftext:
#             print(v)
#         # txt=[]
#         # txt.append(ftext)
#         # print(txt)
#     # if item['text'] == my_unique_id:
#     #     my_item = item
#     #     break
# else:
#     print("sorry i cant hear")