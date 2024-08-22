# dic = {
#     "choda lagana":"Fuck him out",
#     "zindagi":"Life",
#     "duniya":"World",
#     "pani":"Water",
#     "bharwat":"Making Excuses",
#     "bharwagiri":"Making Unbearable Excuses",
#     "kitaab":"Book",
# }

# def lookup_word(word):
#     return dic.get(word, "Word not found in the dictionary")



# while True:
#     user_input = input("Enter a word to look up (or type 'exit' to quit): ").strip()
    
#     if user_input.lower() == 'exit' and user_input == 'cls':
#         print("Goodbye!")
        
#         break
    
#     # Lookup and print the result
#     result = lookup_word(user_input)
#     print(f"{user_input}: {result}")

set1 = set()
set1.add(20)
set1.add(20.0)
set1.add("20")

print(set1)
print(len(set1))