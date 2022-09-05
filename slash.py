# 역슬래시 \ 를 사용하면, 그 뒤의 줄바꿈을 무시하고 해당 행이 이어진다고 판단하게 한다.
long_name_variable = 12345678
if (long_name_variable == 1234567) \
        or (long_name_variable == 123456) \
        or (long_name_variable == 12345678):
    print("longlong")

url1 = "https://www.google.com/search?q=uk"
url2 = "https://www.google.com"  "/search?q=uk"
url3 = "https://www.google.com" \
       "/search?q=uk"
print(url1)
print(url2)
print(url3)
