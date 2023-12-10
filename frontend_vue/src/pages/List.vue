<template lang="">
  <section>
    <div class="container_list">
      <header>
        <nav>
          <ul style="display: flex; gap: 10px">
            <li>Log Out</li>
            <li>Name User</li>
          </ul>
        </nav>
        <img
          :src="actualImage"
          alt=""
          style="height: 270px; margin: 20px 0px 0px 20px"
        />

        <form action="">
          <div v-for="(input, index) in formInputs" :key="index">
            <Input
              :name="input?.name"
              :type="input?.type"
              :required="input?.required"
              :value="input?.value"
              :disabled="input?.disabled"
            />
          </div>
        </form>
      </header>

      <div class="content">
        <aside>aside</aside>
        <div>List</div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref } from "vue";
import Input from "../components/Input.vue";

export default {
  components: {
    Input,
  },
  data() {
    const actualImage = ref(
      "https://t1.uc.ltmcdn.com/es/posts/4/6/5/como_saber_si_mi_husky_es_puro_50564_orig.jpg"
    );

    const formInputs = ref([
      {
        name: "nombre",
        type: "text",
        required: true,
        value: "",
      },
      {
        name: "cliente",
        type: "text",
        required: true,
        value: "",
      },
      {
        name: "nacimiento",
        type: "date",
        required: true,
        value: "",
      },
      {
        name: "edad",
        type: "text",
        required: false,
        value: "",
        disabled: true,
      },
      {
        name: "especie",
        type: "text",
        required: false,
        value: "",
        disabled: false,
      },
      {
        name: "color",
        type: "text",
        required: false,
        value: "",
        disabled: false,
      },
      {
        name: "raza",
        type: "text",
        required: false,
        value: "",
        disabled: false,
      },
      {
        name: "sexo",
        type: "text",
        required: false,
        value: "",
        disabled: false,
      },
      {
        name: "padre",
        type: "text",
        required: false,
        value: "",
        disabled: false,
      },
      {
        name: "madre",
        type: "text",
        required: false,
        value: "",
        disabled: false,
      },
      {
        name: "fecha proxima vacuna",
        type: "text",
        required: false,
        value: "",
        disabled: false,
      },
      {
        name: "enfermedades",
        type: "textarea",
        required: false,
        value: "",
        disabled: true,
      },
      {
        name: "registro de vacunacion",
        type: "textarea",
        required: false,
        value: "",
        disabled: true,
      },
      {
        name: "descripcion",
        type: "textarea",
        required: true,
        value: "",
      },
    ]);

    return {
      actualImage,
      formInputs,
    };
  },
};
</script>

<style lang="css" scoped>
section .container_list {
  background-color: lightgray;
  margin: auto;
  width: 70%;
  min-height: 100vh;
}

nav {
  height: 70px;
  background: pink;
}

form {
  min-height: 600px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  padding: 10px;
}

section .content {
  display: flex;
  background-color: blue;
}

section .content aside {
  display: flex;
  width: 20%;
  background-color: green;
}
</style>
