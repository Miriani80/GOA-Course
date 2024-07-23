# შექმენით ცვლადები რომლებიც ინახება ლოგიკური ოპერაციის შედეგი
# მარცხნიდან მარჯვნივ განვასხვავებთ განზომილებებს რომლებიც
a = 10
b = 5
c = 15

# ლოგიკური ოპერაციების გამოყენება
result_and = (a > b) and (b < c)
result_or = (a > b) or (b > c)

# შედარების ოპერატორების გამოყენება
result_lt = a < b
result_gt = a > b
result_le = a <= b
result_ge = a >= b

# შედეგების დაბეჭდვა
print(f"ლოგიკური ოპერაციები:")
print(f"(a > b) and (b < c) შედეგი: {result_and}")
print(f"(a > b) or (b > c) შედეგი: {result_or}")
print()
print(f"შედარების ოპერატორები:")
print(f"a < b შედეგი: {result_lt}")
print(f"a > b შედეგი: {result_gt}")
print(f"a <= b შედეგი: {result_le}")
print(f"a >= b შედეგი: {result_ge}")