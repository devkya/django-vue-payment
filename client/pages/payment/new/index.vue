<script setup>
const name = ref("");
const amount = ref("");

async function createPayment(event) {
  const forms = document.querySelectorAll(".needs-validation");
  Array.prototype.slice.call(forms).forEach(function (form) {
    if (!form.checkValidity()) {
      event.preventDefault();
      event.stopPropagation();
    }

    form.classList.add("was-validated");
  });

  if (forms[0].checkValidity()) {
    const { data } = await useFetch("/api/payment/", {
      method: "POST",
      body: JSON.stringify({
        name: name.value,
        amount: amount.value,
      }),
    });
    console.log(data);
  }
}
</script>

<template>
  <div>
    <h2>새 결제 생성하기</h2>
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
          <div class="invalid-feedback">Valid Name is required.</div>
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
            <div class="invalid-feedback">Your Amount is required.</div>
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
