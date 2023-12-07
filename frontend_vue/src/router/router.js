import { createRouter, createWebHistory } from "vue-router";
import Presentation from "../pages/Presentation.vue";

const routes = [
  { path: "/", name: "presentation_page", component: Presentation },
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

export default router