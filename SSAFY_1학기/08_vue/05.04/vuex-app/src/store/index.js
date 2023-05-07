import Vue from "vue";
import Vuex from "vuex";

import axios from "axios";
Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		users: [],
	},
	getters: {},
	mutations: {
		CHANGE_USERS(state, payload) {
			state.users = payload;
		},
	},
	actions: {
		getUsers(context, num) {
			axios
				.get(`https://random-data-api.com/api/v2/users?size=${num}`)
				.then((res) => {
					console.log(res.data);
					const users = res.data;
					context.commit("CHANGE_USERS", users);
				});
		},
	},
	modules: {},
});
