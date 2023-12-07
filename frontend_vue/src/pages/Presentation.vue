<template>
  <section class="section_inicio">
    <div class="container">
      <div class="buttons-container">
        <Button
          buttonText="Iniciar sesión"
          :to="{ name: 'login_page' }"
          style="width: 90%; background: var(--color-primario); font-size: 1rem;"
        />
        <Button
          buttonText="Registrarse"
          :to="{ name: 'register_page' }"
          style="width: 90%; background: var(--color-primario); font-size: 1rem;"
        />
      </div>

      <div class="container-image">
        <h1>LISTA APP</h1>
        <img :src="notesPresentation" alt="Presentation" />
      </div>
    </div>
  </section>
</template>

<script>
import notesPresentation from "../assets/notes_presentation.svg";
import Button from "../components/Button.vue";

export default {
  components: {
    Button,
  },
  data() {
    return {
      notesPresentation: notesPresentation,
    };
  },
};
</script>

<style lang="css" scoped>
.container-image {
  width: 80%;
}

h1 {
  margin-bottom: 10px;
}

img {
  height: 80%;
  width: 80%;
}

.buttons-container {
  gap: 10px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  width: 30%;
  border-radius: 50px;
  border-radius: 50px;
background: #ecffff;
box-shadow:  20px 20px 60px #c9d9d9,
             -20px -20px 60px #ffffff;
}
</style>
