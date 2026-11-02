import yaml

info='''
name: 이한
addr: 목동
foods:
  - 맥주
  - 치킨
isname: true
body:
  weight: 59
  height: 172
'''

result = yaml.safe_load(info)

result2=yaml.dump(result, allow_unicode=True) # dict type을 yaml로 변환