from django.shortcuts import render
from rest_framework.decorators import api_view

@api_view(['POST'])
def create(request):
    pass




'''
1. 토큰인증 세션인증 하는방법 
2. 두개의 인증 차이
( 인증 둘다 구현 가능하고 선택할 수도 있게)
3.회원기능 구현(모델 이것저것 다넣어서)
4.★ FBV기반으로 구현
5.재밌는거
- 패스워드 변경시 기존패스워드랑 같으면 변경처리 안되게
'''


