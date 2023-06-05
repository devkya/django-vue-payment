<script setup>
const IMP = window.IMP;
const code = "iamport";
IMP.init(code);
const merchant_uid = "merchant_" + new Date().getTime().toString();
console.log(merchant_uid);

IMP.request_pay(
  {
    merchant_uid,
    name: "주문명: 결제테스트",
    amount: 100,
  },
  function (response) {
    // callback
    console.log(response);
  }
);
</script>

<template>
  <div>
    <h2>결제하기</h2>
  </div>
</template>

<style lang="scss" scoped></style>
