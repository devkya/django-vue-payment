<script setup>
const paymentInfo = ref({});
const config = useRuntimeConfig();

onMounted(async () => {
  const data = await $fetch("http://localhost:8000/payment/1/").catch((err) => {
    console.log(err);
  });
  paymentInfo.value = data;
});

function openPayment() {
  const IMP = window.IMP;
  const code = config.public.PORTONE_SHOP_ID;
  IMP.init(code);
  const props = {
    pg: "tosspayments",
    merchant_uid: paymentInfo.value.merchant_uid,
    name: paymentInfo.value.name,
    amount: paymentInfo.value.amount,
  };

  IMP.request_pay(props, function (response) {
    console.log(response);
  });
}
</script>

<template>
  <div>
    <h4>결제 정보</h4>
    <div>
      <ul>
        <li>{{ paymentInfo.status }}</li>

        <li>{{ paymentInfo.paymentInfo }}</li>
      </ul>
    </div>
    <button class="mt-4 btn btn-primary" @click.stop="openPayment">
      결제하기
    </button>
  </div>
</template>

<style lang="scss" scoped></style>
