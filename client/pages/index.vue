<script setup>
if (process.client) {
  const IMP = window.IMP;
  console.log(IMP);
}
</script>
<template>
  <div>
    <h2>결제 테스트 페이지</h2>
    <Payment />
  </div>
</template>
