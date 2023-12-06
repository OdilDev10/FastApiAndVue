<template>
  <section>
    <div class="container">
      <h1>LISTA APP</h1>

      <div>
        <img :src="notesPresentation" alt="Presentation" />

        <Button buttonText="Iniciar sesión" />
        <Button buttonText="Registrarse" />
      </div>
    </div>
  </section>
</template>

<script>
import notesPresentation from "../assets/notes_presentation.svg";
import Button from "../components/Button.vue";

export default {
  data() {
    return {
      notesPresentation: notesPresentation,
    };
  },
};
</script>

<style lang="css" scoped>
section {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  border-radius: 50px;
  background: linear-gradient(145deg, #ecffff, #c7d8e6);
}

.container {
  width: 65%;
  border-radius: 50px;
  background: linear-gradient(145deg, #ecffff, #c7d8e6);
  box-shadow: 20px 20px 60px #bcccd9, -20px -20px 60px #feffff;
  text-align: center;
  padding: 60px;
}

h1 {
  margin-bottom: 10px;
}

img {
  height: 50%;
  width: 50%;
}
</style>
