export default defineEventHandler(async (event) => {
  console.log("payment()...");
  const { formData } = await readBody(event);
  console.log(formData);
  const uri = "http://localhost:8000/payment/pay/";
  const { data } = await $fetch(uri, {
    method: "POST",
    body: JSON.stringify(event),
    headers: {
      "Content-Type": "application/json",
    },
  });
  return data;
});
