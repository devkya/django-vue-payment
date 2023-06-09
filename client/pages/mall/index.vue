<script setup>
import Paginate from "vuejs-paginate-next";
import { useProductStore } from "~/stores/product";

onMounted(async () => {
  await productStore.getProducts();
  pages.value = productStore.pages;
});

const productStore = useProductStore();
const search = ref("");
const pages = ref(0);
const products = computed(() => productStore.products);

function clickCallback(pageNum) {
  console.log(pageNum);
  productStore.loadProduct(pageNum);
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}

function searchProducts() {
  console.log("searchProducts()...");
}
</script>

<template>
  <div>
    <div class="row">
      <form
        class="col-8 col-lg-4 d-flex flex-row"
        @submit.prevent="searchProducts"
      >
        <input
          v-model="search"
          class="form-control form-control-white"
          placeholder="상품명을 검색하세요"
        />
        <button type="button" class="btn btn-secondary">Search</button>
      </form>
    </div>

    <div class="row">
      <div
        v-for="(product, index) in products"
        :key="index"
        class="col-sm-6 col-lg-4 my-2"
      >
        <ProductItemCard :product="product"></ProductItemCard>
      </div>
    </div>
    <div class="mt-3 d-flex align-items-center justify-content-center">
      <Paginate
        :page-count="pages"
        :page-range="10"
        :click-handler="clickCallback"
      ></Paginate>
    </div>
  </div>
</template>

<style lang="scss" scoped></style>
