<script setup>
// const status = ref([
//   { name: "미결제", value: "ready" },
//   { name: "결제완료", value: "paid" },
//   { name: "결제취소", value: "cancelled" },
//   { name: "결제실패", value: "failed" },
// ]);
const name = ref("");
const amount = ref("");

function createPayment(event) {
  const forms = document.querySelectorAll(".needs-validation");
  console.log(forms);
  Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener(
      "submit",
      function (event) {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
}

// function validateTest() {}
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
          <div class="invalid-feedback">Valid first name is required.</div>
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
            <div class="invalid-feedback">Your username is required.</div>
          </div>
        </div>
      </div>

      <hr class="my-4" />

      <button class="w-100 btn btn-primary btn-lg" type="submit">
        Create New Payment
      </button>
    </form>
  </div>
</template>

<style lang="scss" scoped></style>
