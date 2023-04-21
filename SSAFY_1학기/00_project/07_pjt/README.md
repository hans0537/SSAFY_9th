# 07_pjt

구현 방식 & 느낀점

- DRF(Django Rest Framewordk)를 이용한 API Server 제작하면서 데이터를 효과적을 넘겨주는 방법을 배움

- REST API를 통해 서버에서 클라이언트가 필요로 하는 데이터들을 요구사항에 맞게 api를 제작하는 과정이 매우 흥미롭고 데이터를 조작하는 과정에서도 재미를 느꼈다.

- Django 에서는 Serializer를 통해 데이터를 편하게 주고 받을수 있는점에선 매우 편리했으나 클라이언트의 추가적인 요구사항에 맞게 구현을 하는것은 까다로웠다.

- 예로들어 필요한 필드만 보여주기 위해선 나는 to_representation을 사용했다.

    ```
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        for dic in rep['movies']:
            print(dic)
            dic.pop('overview')
        return rep
    ```
    위 코드와 같이 해당 정보를 가져온후 필요 없는 필드를 pop하는 방식으로 가져왔다. 따로 새로운 Serializer를 생성할 수 있었지만 불필요한 Class 선언 하는 느낌이 들어 기존에 있는 Class를 활용하여 해당 요청일 때만 가공해주는 방식으로 구현했다.

<br>
향후 추가 개발 사항

- 외부 API를 불러와서 실시간 정보를 제공해주는 api를 제작 할 수 있을것 같다. 
