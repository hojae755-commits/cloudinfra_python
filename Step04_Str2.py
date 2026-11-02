import json

info = '''
{
    "name": "이한",
    "addr": "목동",
    "foods": ["맥주", "치킨", "피자"]
}
'''

result=json.loads(info) # json을 dict type으로 변환

print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])

result2=json.dumps(result) # dict type을 json으로 변환

# json을 받으면 해석이 가능 문자열이 json 형식이 아니다? 그럼 오류, json을 해석했는데 내가 해석 불가능한 구조다? 그럼오류