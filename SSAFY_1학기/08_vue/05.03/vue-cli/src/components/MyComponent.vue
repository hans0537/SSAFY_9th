<template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <MyChild static-props="component(부모) 에서 child로"
    :dynamic-props="dynamicProps"
    @child-to-parent="parentGetEvent"
    @child-input="getDynamicData"/>

    <!-- :동적 변수 (바인딩) 은 "" 따옴표는 그냥 포장지이고 자바스크립트 구문이다
          진짜 데이터는 "" 안에 값이라 숫자가 넘어간다.
          문자열을 보내려면 " '1' " 따옴표 한번 더 붙여 주면 된다. 
    <MyChild static-props="1"
    :dynamic-props="1"
    @child-to-parent="parentGetEvent"/>
    -->
  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name: 'MyComponent',
  components: {
    MyChild,
  },
  data: function() {
    return {
      dynamicProps: "It is a data"
    }
  },
  methods: {
    parentGetEvent: function(inputData) {
      console.log('자식 컴포넌트에서 발생한 이벤트')
      console.log(`child에서 보낸 ${inputData} 를 받음`)
    },
    getDynamicData: function(input) {
      console.log(`child 에서 입력한 ${input} 출력`)
    }
  }
}

</script>

<style>
  .border {
    border: solid;
  }
</style>
