<template lang="">
  <section class="section_inicio">
    <div class="container" style="flex-direction: column">
      <div
        style="
          display: flex;
          flex-direction: column;
          gap: 13px;
          justify-content: center;
          align-items: center;
        "
      >
        <Title title="Register" />
        <img :src="authenticationImg" alt="Authorization" />
        <Input style="width: 50%" name="email" type="email" required />
        <Input style="width: 50%" name="username" type="text" required />
        <Input style="width: 50%" name="password" type="password" required />

        <div style="display: flex; justify-content: center; gap: 7px">
          <Button
            buttonText="Register"
            style="background: var(--color-suave)"
            :to="{ name: 'login_page' }"
          />
          <Button
            buttonText="Login"
            style="background: var(--color-primario)"
            :to="{ name: 'login_page' }"
          />
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import Button from "../components/Button.vue";
import Input from "../components/Input.vue";
import Title from "../components/Title.vue";
import authenticationImg from "../assets/authentication.svg";

export default {
  components: {
    Button,
    Input,
    Title,
  },
  data() {
    return {
      authenticationImg: authenticationImg,
    };
  },
};
</script>
<style lang="css">
img {
  height: 200px;
}
</style>
