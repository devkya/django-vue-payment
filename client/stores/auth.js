import { defineStore } from "pinia";
export const useAuthStore = defineStore("auth", {
  state: () => ({ user: null }),
  getters: {
    getUser: (state) => state.user,
  },
  actions: {
    logout() {
      this.user = null;
    },
  },
  persist: true,
});
