<script setup>
const data = ref({});
onMounted(async () => {
  data.value = await $fetch("http://localhost:8000/payment/1/").catch((err) => {
    console.log(err);
  });
});
</script>
<template>
  <div>
    <h2>결제 내역</h2>
    <div>
      <ul>
        <li>{{ data.status }}</li>
        <li>결제 아이디 : {{ data.merchant_uid }}</li>
        <li>결제명 : {{ data.name }}</li>
        <li>결제금액 : {{ data.amount }}원</li>
      </ul>
    </div>
  </div>
</template>
