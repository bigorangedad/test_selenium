import yaml
#
# print(yaml.load("""
#     - Hesperiidae
#     - Papilionidae
#     - Apatelodidae
#     - Epiplemidae
#     """, Loader=yaml.FullLoader))

# print(yaml.load(open("tst_1.yml"), Loader=yaml.FullLoader))

# with open("demo.yml", "w") as f:
#     print(yaml.dump(data=['public', 'private', {'b': 123}], stream=f))

print(yaml.safe_load(open("demo.yml")))

