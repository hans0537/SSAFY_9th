import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Happeed from "../views/Happeed.vue";
import Happling from "../views/Happling.vue";

Vue.use(VueRouter);

const routes = [
	{
		path: "/",
		name: "home",
		component: Home,
	},
	{
		path: "/happeed",
		name: "happeed",
		component: Happeed,
		beforeEnter(to, from, next) {
			if (from.name === "happling") {
				alert("이전 단계로 돌아갈 수 없습니다.");

				return;
			}

			next();
		},
	},
	{
		path: "/happling",
		name: "happling",
		component: Happling,
	},
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes,
});

export default router;
