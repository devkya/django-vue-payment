import { defineStore } from "pinia";
export const useProductStore = defineStore("product", {
  state: () => ({
    products: [],
    product: {},
  }),

  actions: {
    async getProducts() {
      try {
        const res = await $fetch("http://localhost:8000/mall/products/", {
          method: "GET",
        });
        this.products = res;
      } catch (err) {
        console.log(err);
      }
    },
  },
});
