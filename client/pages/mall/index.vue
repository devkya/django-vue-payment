<script setup>
import { useProductStore } from "~/stores/product";

const productStore = useProductStore();
const products = ref([]);
onMounted(async () => {
  await productStore.getProducts();
  products.value = productStore.products;
});
</script>

<template>
  <div>
    <ul>
      <li v-for="(product, index) in products" :key="index">
        {{ product.name }} / {{ product.price }}원
      </li>
    </ul>
  </div>
</template>

<style lang="scss" scoped></style>
