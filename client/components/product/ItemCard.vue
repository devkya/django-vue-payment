<script setup>
const props = defineProps({
  product: {
    type: Object,
    required: true,
  },
});
const { product } = toRefs(props);
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
        <a href="#" class="btn btn-primary">장바구니에 담기</a>
      </p>
    </div>
  </div>
</template>
