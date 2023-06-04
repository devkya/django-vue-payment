<script setup>
if (process.client) {
  const IMP = window.IMP;
  const code = "iamport";
  IMP.init(code);
  const merchant_uid = "merchant_" + new Date().getTime();
  console.log(merchant_uid);
}
</script>
<template>
  <div>
    <h2>결제하기</h2>
  </div>
</template>
