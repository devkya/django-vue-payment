// export default defineEventHandler(async (event) => {
//   console.log("payment()...");
//   const { formData } = await readBody(event);
//   console.log(formData);
//   const uri = "http://localhost:8000/payment/pay/";
//   const { data } = await $fetch(uri, {
//     method: "POST",
//     body: JSON.stringify(event),
//     headers: {
//       "Content-Type": "application/json",
//     },
//   });
//   return data;
// });

export default defineEventHandler((event) => {
  console.log("event()...", event);
  const uri = "http://localhost:8000/payment/pay/";
  const { data } = $fetch(uri, {
    method: "POST",
  }).catch((err) => {
    console.log(err);
  });
  console.log(data);
  return { data: "test" };
});
