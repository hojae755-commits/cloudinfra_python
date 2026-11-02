nums=[10, 20, 30, 40, 50]
names=["kim", "lee", "park", "choi", "jung"]

for item in nums:
    print(item)

r1=range(len(nums)) # 0~4까지
for item in r1:
    print(item, nums[item]) # 인덱스와 값 출력