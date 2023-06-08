<script setup>
const name = ref("");
const amount = ref("");

async function createPayment(event) {
  const form = document.querySelectorAll(".needs-validation")[0];

  if (!form.checkValidity()) {
    event.preventDefault();
    event.stopPropagation();
    form.classList.add("was-validated");
  } else {
    // const { data, error } = await useFetch("/api/payment"); // XXX: server/api/payment 작동안됨
    const uri = "http://localhost:8000/payment/pay/";
    const res = await $fetch(uri, {
      method: "POST",
      body: {
        name: name.value,
        amount: amount.value,
      },
    }).catch((error) => {
      console.log(error);
    });
  }
}
</script>

<template>
  <div>
    <div>
      <h2>새 결제 생성하기</h2>
    </div>
    <form class="needs-validation" novalidate @submit.prevent="createPayment">
      <div class="row g-3">
        <div class="col-sm-12">
          <label for="name" class="form-label">Name</label>
          <input
            id="name"
            v-model="name"
            type="text"
            class="form-control"
            placeholder="결제명"
            required
          />
          <div class="invalid-feedback">Name is required.</div>
        </div>

        <div class="col-12">
          <label for="username" class="form-label">Amount</label>
          <div class="input-group has-validation">
            <input
              id="amount"
              v-model="amount"
              type="text"
              class="form-control"
              placeholder="결제 금액"
              required
            />
            <div class="invalid-feedback">Amount is required.</div>
          </div>
        </div>
      </div>

      <button class="mt-4 btn btn-primary" type="submit">
        Create New Payment
      </button>
    </form>
  </div>
</template>

<style lang="scss" scoped></style>
