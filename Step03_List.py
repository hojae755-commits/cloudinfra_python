nums=[10, 20, 30]
names=["이한", "원숭이띠"]
datas=[10, "xxx", True]

nums.append(40) # 리스트에 값 추가
names.insert(1, "이란") # 리스트에 값 삽입
nums_len=len(nums)
name0=names[0]
names.remove("이란") # 리스트에서 값 제거
result=nums.pop() # 리스트에서 마지막 값 제거
nums.push(result) # 리스트에 값 추가