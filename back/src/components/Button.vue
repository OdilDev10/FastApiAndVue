<template>
  <button>{{ buttonText }} A</button>
</template>

<script>
export default {
  props: {
    buttonText: {
      type: String,
      default: "Login", // Valor por defecto si no se proporciona ninguna prop
    },
  },
};
</script>

<style scoped>
/* Estilos para tu botón */
</style>
