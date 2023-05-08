import Vue from 'vue'
import Vuex from 'vuex'
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: '아메리카노',
        price: 3000,
        selected: false,
        image: 'https://source.unsplash.com/featured/?americano'
      },
      {
        title: '카페라떼',
        price: 3500,
        selected: false,
        image: 'https://source.unsplash.com/featured/?cafelatte'
      },
      {
        title: '카푸치노',
        price: 3800,
        selected: false,
        image: 'https://source.unsplash.com/featured/?cappuccino'
      },
      {
        title: '아이스티',
        price: 4000,
        selected: false,
        image: 'https://source.unsplash.com/featured/?IcedTea'
      },
    ],
    sizeList: [
      {
        name: 'Small',
        price: 0,
        selected: false,
      },
      {
        name: 'medium',
        price: 500,
        selected: false,
      },
      {
        name: 'Large',
        price: 1000,
        selected: false,
      },
    ],
    optionList: [
      {
        type: '샷',
        price: 500,
        count: 0,
      },
      {
        type: '바닐라 시럽',
        price: 600,
        count: 0,
      },
      {
        type: '카라멜 시럽',
        price: 600,
        count: 0,
      },
    ],
    selectedMenu: {},
    selectedSize: {},
  },
  getters: {
    totalOrderCount(state) {
      return state.orderList.length
    },
    totalOrderPrice(state) {
      return state.orderList.reduce((sum, order) => {

        return sum + order.menu.price + order.size.price 
        + order.options[0].price * order.options[0].count
        + order.options[1].price * order.options[1].count
        + order.options[2].price * order.options[2].count
      }, 0)
    }
  },
  mutations: {
    UPDATE_MENU_LIST(state, selectedMenu) {
      state.menuList = state.menuList.map((menu) => {
        if(menu.title === selectedMenu.title) {
          menu.selected = !menu.selected
          state.selectedMenu = selectedMenu
        }else {
          menu.selected = false
        }
        return menu
      })
    },

    UPDATE_SIZE_LIST(state, selectedSize){
      state.sizeList = state.sizeList.map((size) => {
        if(size.name === selectedSize.name) {
          size.selected = !size.selected
          state.selectedSize = selectedSize
        }else{
          size.selected = false
        }
        return size
      })
    },

    INCREASE_OPTION_LIST(state, selectedOption){
      state.optionList = state.optionList.map((option) => {
        if(option.type === selectedOption.type) {
          option.count += 1
        }
        return option
      })
    },

    DECREASE_OPTION_LIST(state, selectedOption){
      state.optionList = state.optionList.map((option) => {
        if(option.type === selectedOption.type) {
          if(option.count > 0) {
            option.count -= 1
          }
        }
        return option
      })
    },

    ADD_ORDER(state) {
      state.orderList.push({
        menu: state.selectedMenu,
        size: state.selectedSize,
        options: _.cloneDeep(state.optionList),
      })

      state.optionList = state.optionList.map((option) => {
        if(option.count > 0) {
            option.count = 0
        }
        return option
      })
    },


    LOAD_ORDER_LIST(state) {
      const parse = JSON.parse(localStorage.getItem('orderList'))
      state.orderList = parse
    }
  },
  actions: {
    selectMenu(context, menu) {
      context.commit("UPDATE_MENU_LIST", menu)
    },
    selectSize(context, size) {
      context.commit("UPDATE_SIZE_LIST", size)
    },
    increaseCount(context, option) {
      context.commit("INCREASE_OPTION_LIST", option)
    },
    decreaseCount(context, option) {
      context.commit("DECREASE_OPTION_LIST", option)
    },


    addOrder(context) {
      console.log(this.state.selectedMenu)
      if(this.state.selectedMenu.selected) {
        context.commit("ADD_ORDER")
        context.dispatch("saveToLocalStorage")
      }else{
        alert('커피를 선택하세요 !!')
      }
    },

    saveToLocalStorage(context){
      const jsonMenu = JSON.stringify(context.state.orderList)
      localStorage.setItem('orderList', jsonMenu)
    },
    loadOrderList(context) {
      context.commit('LOAD_ORDER_LIST')
    }
  },
  modules: {
  }
})
