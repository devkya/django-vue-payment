<script setup>
import { useProductStore } from "@/stores/product";

const productStore = useProductStore();
const props = defineProps({
  product: {
    type: Object,
    required: true,
  },
});
const { product } = toRefs(props);

async function addCart() {
  console.log("addCart()...");
  const res = await productStore.addCart(product.value.id);
  console.log(res);
}
</script>

<template>
  <div class="card">
    <img
      v-if="!!product.photo"
      :src="product.photo"
      class="img-thumbnail img-fluid card-img-top"
      :alt="product.name"
      style="width: 100%"
    />
    <div class="card-body">
      <span class="mb-1 badge rounded-pill bg-secondary">
        {{ product.category_name }}
      </span>
      <h5 class="text-truncate card-title">
        {{ product.name }}
      </h5>
      <p
        class="mt-3 card-text d-flex justify-content-between align-items-center"
      >
        {{ product.price.toLocaleString() }}원
        <a class="btn btn-primary" @click.stop="addCart">장바구니에 담기</a>
      </p>
    </div>
  </div>
</template>
