
with open("headers.txt", 'r') as file:
    headers_unformatted = [header.strip() for header in file]


organized_headers = dict()
for header in headers_unformatted:
    key, value = header.split(": ")
    organized_headers[key] = value

print("{")
for k, v in organized_headers.items():
    print(f"'{k}'", ":", f"'{v}',")
print("}")

