<script setup>
import { useAuthStore } from "~/stores/auth";
const authStore = useAuthStore();
const route = useRoute();

const user = computed(() => authStore.getUser);

function logout() {
  authStore.logout();
  route.push("/");
}
</script>

<template>
  <div>
    <div class="container">
      <header
        class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom"
      >
        <a
          href="/"
          class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none"
        >
          <span class="fs-4">Devkya 결제 시스템</span>
        </a>

        <ul class="nav nav-pills">
          <li class="nav-item">
            <NuxtLink
              class="nav-link"
              :class="$route.name == 'index' ? 'active' : ''"
              to="/"
              >Home</NuxtLink
            >
          </li>
          <li class="nav-item">
            <NuxtLink
              class="nav-link"
              :class="$route.name == 'check' ? 'active' : ''"
              to="/check"
              >Complete</NuxtLink
            >
          </li>

          <li class="nav-item">
            <NuxtLink
              class="nav-link"
              :class="$route.name == 'payment' ? 'active' : ''"
              to="/payment"
              >Payment</NuxtLink
            >
          </li>

          <li v-if="!user" class="nav-item">
            <NuxtLink
              class="nav-link"
              :class="$route.name == 'payment' ? 'active' : ''"
              to="/account/login"
              >Login</NuxtLink
            >
          </li>
          <li v-if="!user" class="nav-item">
            <NuxtLink
              class="nav-link"
              :class="$route.name == 'payment' ? 'active' : ''"
              to="/account/signup"
              >Sign Up</NuxtLink
            >
          </li>

          <li v-else class="nav-item">
            <a class="nav-link" href="#" @click="logout">Logout</a>
          </li>
        </ul>
      </header>
    </div>

    <div class="container">
      <slot />
    </div>

    <hr />

    &copy; 2023. Developed by Devkya
  </div>
</template>

<style lang="scss" scoped></style>
