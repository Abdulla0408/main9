# ----------------------------------------------------------------------------------------------

# gene - 1

# k,n = map(int,input("k va n sonlarini kiriting: ").split())
# num = [k for i in range(n)]
# print(num)

# ----------------------------------------------------------------------------------------------

# gene - 2

# def num():
#     count = 0
#     a,b = map(int,input("a va b sonlarini kiriting: ").split())
#     for i in range(a,b+1):
#         count = count + 1
#         if a < b:
#             yield i
# print(list(num()))

# ----------------------------------------------------------------------------------------------

# gene - 3

# def numbers():
#     count = 0
#     a, b = map(int, input("A va B sonlarini kiriting: ").split())
#     for i in range(a - 1, b):
#         yield i[-1]
# print(list(numbers()))

# ----------------------------------------------------------------------------------------------

# gene - 4

# sweets_price = int(input("How much sweets a kilo? "))
# sweets = [sweets_price * i  for i in range(1,10+1)]
# print(sweets)

# ----------------------------------------------------------------------------------------------

# gener - 5

# word = "hello world"
# gener = [i.upper() for i in word]
# print(gener)

# ----------------------------------------------------------------------------------------------

# gener - 6

# word = "HeLlo wORlD"
# capital_letter = []
# small_letter = []
#
# katta = [capital_letter.append(i) if i.isupper() else False for i in word]
# kichik = [small_letter.append(i) if i.islower() else False for i in word]
# print(capital_letter)
# print(small_letter)



# ----------------------------------------------------------------------------------------------

# gene-7

# num = [i**3 for i in range(1,21) ]
# print(num)

# ----------------------------------------------------------------------------------------------

# gene-8

# def juft_ikki():
#     for i in range(1,21):
#         if i % 2 == 0:
#             yield i / 2
# print(list(juft_ikki()))

# ----------------------------------------------------------------------------------------------

# gene-9

# num_dict = ((i, i**2) for i in range(1,11))
# print(dict(num_dict))

# ----------------------------------------------------------------------------------------------

# gene - 10

# word = "salom dunyo"
# words = [(i, i.upper()) for i in word if i.isalpha()]
# print(dict(words))