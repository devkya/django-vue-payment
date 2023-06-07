<script setup></script>

<template>
  <div>
    <div>
      <div>
        <h2>새 결제 생성하기</h2>
      </div>
      <form class="needs-validation" novalidate @submit.prevent="createPayment">
        <div class="row g-3">
          <div class="col-sm-12">
            <label for="name" class="form-label">사용자 이름*</label>
            <input
              id="name"
              v-model="name"
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
                id="password1"
                v-model="password1"
                type="password"
                class="form-control"
                placeholder="비밀번호를 입력하세요."
                required
              />
              <div class="invalid-feedback">Password1 is required.</div>
            </div>
          </div>
          <div class="col-12">
            <label for="username" class="form-label">비밀번호 확인*</label>
            <div class="input-group has-validation">
              <input
                id="password2"
                v-model="password2"
                type="password"
                class="form-control"
                placeholder="비밀번호를 다시 한번 입력하세요."
                required
              />
              <div class="invalid-feedback">Password2 is required.</div>
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
