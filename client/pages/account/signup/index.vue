<script setup>
const router = useRouter();
const username = ref("");
const password = ref("");

async function createAccount() {
  const form = document.querySelectorAll(".needs-validation")[0];

  if (!form.checkValidity()) {
    event.preventDefault();
    event.stopPropagation();
    form.classList.add("was-validated");
  } else {
    const uri = "http://localhost:8000/accounts/signup/";
    const res = await $fetch(uri, {
      method: "POST",
      body: {
        username: username.value,
        password: password.value,
      },
    }).catch((error) => {
      console.log(error);
    });

    if (res) {
      console.log(res);
      router.push("/account/login");
    }
  }
}
</script>

<template>
  <div>
    <div>
      <div>
        <h2>새 결제 생성하기</h2>
      </div>
      <form class="needs-validation" novalidate @submit.prevent="createAccount">
        <div class="row g-3">
          <div class="col-sm-12">
            <label for="username" class="form-label">사용자 이름*</label>
            <input
              id="username"
              v-model="username"
              type="text"
              class="form-control"
              placeholder="사용자 이름을 입력하세요."
              required
            />
            <div class="invalid-feedback">Name is required.</div>
          </div>

          <div class="col-12">
            <label for="username" class="form-label">비밀번호*</label>
            <div class="input-group has-validation">
              <input
                id="password"
                v-model="password"
                type="password"
                class="form-control"
                placeholder="비밀번호를 입력하세요."
                required
              />
              <div class="invalid-feedback">Password is required.</div>
            </div>
          </div>
        </div>

        <button class="mt-4 btn btn-primary" type="submit">
          Create New Account
        </button>
      </form>
    </div>
  </div>
</template>

<style lang="scss" scoped></style>
