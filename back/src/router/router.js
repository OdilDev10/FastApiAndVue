import { createRouter, createWebHistory } from "vue-router";
import Presentation from "../pages/Presentation.vue";

const routes = [
  { path: "/", name: "presentation_page", component: Presentation },
  {
    path: "/login",
    name: "login_page",
    component: () => import("../pages/Login.vue"),
  },
  {
    path: "/register",
    name: "register_page",
    component: () => import("../pages/Register.vue"),
  },
  {
    path: "/list",
    name: "list_page",
    component: () => import("../pages/List.vue"),
  },
];

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
