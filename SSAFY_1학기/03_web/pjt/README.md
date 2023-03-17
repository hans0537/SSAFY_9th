# 03_pjt

- 01_nav_footer.html

  - Bootstrap Navbar Component 반응형 네비게이션 바 사용.
  - 화면 상단 고정은 sticky-top 클래스, 하단 고정은 fixed-bottom 클래스 사용
  - 각각의 페이지 이동은 a태그 활용
  - 추가적으로 activate 클래스로 해당 기능의 페이지 일때 
  강조
  - Login 클릭시 모달창 생성은 Modal과 Forms component를 사용
  - 각각의 뼈대들을 부트스트랩에서 가져온뒤 화면에 적절하게 배치하는 작업이 매우 재밌고,
    편리하였다. 또한 docs에 친절히 클래스들의 역할이 잘 나와있기에 편리하게 작업을 할 수 있다.
  - 예) width 768px 미만 일때 반응형 네비게이션바
        navbar-expand-(사이즈) : width 사이즈에 따라 네비게이션 모양이 변경
        따라서 navbar-expand-md를 주어 해결!

</br></br>
- 02_home.html

  - carousel slide를 활용하여 header이미지 배치.
  - 추가적으로 data-bs-interval="3000"을 주어 3초뒤에 자동으로 이미지 슬라이드 적용
  - 섹션 내부의 카드 요소들을 적절하게 배치하고 반응형 디자인이 좀 까다로웠다.
  - 576px 기준이므로 각각의 카드요소엔 
    576px 미만일때 col-12, 이상일때 col-sm-4 두개의 클래스를 주었다.
  - 추가적으로 section부분의 마진을 주어 크기를 적절히 조절

</br></br>
- 03_community.html

  - 게시판 목록은 992px이상일때만 1/6 너비 이므로 col-lg-2
  - section 부분에서 992px미만이면 article 이상이면 tables content로 화면에 출력하여야 한다.
  - 이때 새로운 부트스트랩 클래스인 none과 block을 활용하여 기준 width일때 해당 요소를 보여주거나 숨김 처리가 가능하다.
  - 즉 992px미만 일경우 article만 보여줄려면 table요소를 일단 d-none 숨김처리 한뒤
  - 992px이상일때 article은 d-lg-none해서 숨겨주고, table은 d-lg-block으로 보여준다.
  - 그리고 section에 나머지 10칸 너비를 할당해주면 (col-lg-10) 요구사항처럼 리스트 옆에 테이블이 위치한다.
  - page요소는 정렬해주는 justify-content-center를 활용하여 간단하게 수평중앙 정렬했다.
