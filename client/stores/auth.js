import { defineStore } from "pinia";
export const useAuthStore = defineStore("auth", {
  state: () => ({ user: null }),
  getters: {
    getUser: (state) => state.user,
  },
  actions: {
    async login(data) {
      try {
        const res = await $fetch("http://localhost:8000/accounts/login/", {
          method: "POST",
          body: data,
        });
        console.log(res);
        this.user = res.user;
        return res;
      } catch (err) {
        console.log(err);
      }
    },
    logout() {
      this.user = null;
    },
  },
  persist: true,
});
