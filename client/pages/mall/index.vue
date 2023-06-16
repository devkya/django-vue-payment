<script setup>
import Paginate from "vuejs-paginate-next";
import { useProductStore } from "~/stores/product";

onMounted(async () => {
  await productStore.getProducts();
  pages.value = productStore.pages;
});

const isMsg = ref("hidden");
const productStore = useProductStore();
const search = ref("");
const pages = ref(0);
const products = computed(() => productStore.products);

async function clickCallback(pageNum) {
  console.log(pageNum);
  await productStore.loadProduct(pageNum);
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}

async function searchProducts() {
  // EDIT : 수정해야 함
  console.log("searchProducts()...", search.value);
  await productStore.searchProducts(search.value);
  pages.value = productStore.pages;
}
</script>

<template>
  <div>
    <div class="row">
      <form
        class="col-12 col-lg-4 d-flex flex-row"
        @submit.prevent="searchProducts"
      >
        <input
          v-model="search"
          class="form-control form-control-white"
          placeholder="상품명을 검색하세요"
        />
        <button type="submit" class="mx-1 btn btn-secondary">Search</button>
      </form>
    </div>

    <div class="row">
      <div class="col-12">
        <div
          class="alert alert-primary text-center"
          :style="{ visibility: isMsg }"
          role="alert"
        >
          상품을 장바구니에 추가했습니다!
        </div>
      </div>
    </div>

    <div class="row">
      <div
        v-for="(product, index) in products"
        :key="index"
        class="col-sm-6 col-lg-4 my-1"
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
