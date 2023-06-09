import { defineStore } from "pinia";
export const useProductStore = defineStore("product", {
  state: () => ({
    products: [],
    product: {},
    pages: 0,
    curPage: 1,
  }),

  actions: {
    async loadProduct(page) {
      this.curPage = page;
      await this.getProducts();
    },
    async getProducts() {
      try {
        const res = await $fetch(
          `http://localhost:8000/mall/products/?page=${this.curPage}`,
          {
            method: "GET",
          }
        );
        this.products = res.results;
        this.pages = res.pages;
      } catch (err) {
        console.log(err);
      }
    },
    // EDIT : 수정해야 함
    async searchProducts(search) {
      try {
        const res = await $fetch(
          `http://localhost:8000/mall/products/?search=${search}`,
          {
            method: "GET",
          }
        );
        this.products = res.results;
        this.pages = res.pages;
      } catch (err) {
        console.log(err);
      }
    },
  },
});
