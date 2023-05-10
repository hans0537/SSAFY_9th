import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate"; // vuex plugin
import _ from "lodash";

Vue.use(Vuex);

const orderState = createPersistedState({
	// key를 변경
	key: "coffee-app",
	// 저장 위치를 세션 스토리지로 변경
	storage: window.sessionStorage,
	// 상태중 일부만 저장 (사용 x)
	// reducer: (state) => ({
	// 	message: state.message,
	// }),
});

export default new Vuex.Store({
	plugins: [orderState],
	state: {
		optionList: [
			{
				title: "샷",
				count: 0,
				price: 500,
			},
			{
				title: "바닐라 시럽",
				count: 0,
				price: 500,
			},
			{
				title: "카라멜 시럽",
				count: 0,
				price: 500,
			},
		],
		orderList: [],
		menuList: [
			{
				title: "아메리카노",
				price: 3000,
				selected: false,
				image: require("@/assets/ame.jpg"),
			},
			{
				title: "라떼",
				price: 4000,
				selected: false,
				image: require("@/assets/latte.jpg"),
			},
			{
				title: "카푸치노",
				price: 4500,
				selected: false,
				image: require("@/assets/capu.jpg"),
			},
			{
				title: "딸기 딜라이트 요거트 블렌디드",
				price: 4500,
				selected: false,
				image: require("@/assets/berry.jpg"),
			},
		],
		sizeList: [
			{
				name: "small",
				price: 0,
				selected: false,
			},
			{
				name: "medium",
				price: 500,
				selected: false,
			},
			{
				name: "large",
				price: 1000,
				selected: false,
			},
		],
		selectedMenu: {},
		selectedSize: {},
	},
	getters: {
		totalOrderCount(state) {
			return state.orderList.length;
		},
		totalOrderPrice(state) {
			return state.orderList.reduce((sum, order) => {
				sum += order.menu.price + order.size.price;
				console.log(order.optionList);

				// reduce로 옵션 가격 총합 구하기
				sum += order.optionList.reduce((osum, option) => {
					if (option.count > 0) {
						osum += option.count * option.price;
						console.log(osum);
					}
					return osum;
				}, 0);

				return sum;
			}, 0);
		},
	},
	mutations: {
		addOrder(state) {
			state.orderList.push({
				menu: state.selectedMenu,
				size: state.selectedSize,

				// 옵션 정보 딥카피
				optionList: _.cloneDeep(state.optionList),
			});

			// 옵션 정보 초기화 해서 얕은 복사 일어나지 않았는지 보기
			state.optionList = state.optionList.map((option) => {
				option.count = 0;

				return option;
			});
		},
		updateMenuList(state, selectedMenu) {
			state.menuList = state.menuList.map((menu) => {
				if (menu.title === selectedMenu.title) {
					menu.selected = true;
					state.selectedMenu = selectedMenu;
				} else {
					menu.selected = false;
				}
				return menu;
			});
		},
		updateSizeList(state, selectedSize) {
			state.sizeList = state.sizeList.map((size) => {
				if (size.name === selectedSize.name) {
					size.selected = true;
					state.selectedSize = selectedSize;
				} else {
					size.selected = false;
				}
				return size;
			});
		},
		increaseOption(state, optionTitle) {
			state.optionList = state.optionList.map((option) => {
				if (option.title === optionTitle) {
					option.count += 1;
				}
				return option;
			});
		},
		decreaseOption(state, optionTitle) {
			state.optionList = state.optionList.map((option) => {
				if (option.title === optionTitle) {
					option.count -= 1;
				}
				return option;
			});
		},
	},
	actions: {
		selectMenu(context, selectedMenu) {
			context.commit("updateMenuList", selectedMenu);
		},
		selectSize(context, selectedSize) {
			context.commit("updateSizeList", selectedSize);
		},
		addOrder(context) {
			context.commit("addOrder");
		},
	},
	modules: {},
});
