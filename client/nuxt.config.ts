// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  css: ["~/assets/styles/main.scss"],
  app: {
    head: {
      title: "Devkya 쇼핑몰",
      script: [
        {
          src: "https://cdn.iamport.kr/v1/iamport.js",
        },
      ],
    },
  },
});
