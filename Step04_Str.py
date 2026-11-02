text="     Cloud Infra     "
result2=text.strip() # 양쪽 공백 제거
myIp="192.168.0.2"
result2=myIp.split(".") # 점(.)을 기준으로 문자열 분리 후 리스트로 변환
result3=":".join(result2) # 리스트를 ":"로 연결하여 문자열로 변환
result4="hello mimi!".replace("mi", "ma")
result5="python".upper() # 대문자로 변환
result6="PYTHON".lower() # 소문자로 변환