<template>
  <button :disabled="disabled" @click="navigate" :style="style">{{ buttonText }}</button>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  props: {
    buttonText: {
      type: String,
      default: "buttonText",
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    to: {
      type: [String, Object],
      default: null,
    },
    style: {
      type: String,
      default: '',
    },
  },
  setup(props) {
    const router = useRouter();

    const navigate = () => {
      if (props.to) {
        router.push(props.to);
      } else {
        console.warn('La propiedad "to" no está definida para la navegación.');
      }
    };

    return {
      navigate,
    };
  },
};
</script>

<style scoped>
button {
  height: 50px;
  width: 150px;
  border-radius: 15px;
  outline: none;
  border: none;
  font-weight: 700;
  cursor: pointer;
}

/* Estilos para tu botón */
</style>
