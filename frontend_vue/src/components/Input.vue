<template lang="">
  <div class="container_input">
    <label :for="name">{{ capitalizeFirstLetter(name) }}</label>

    <textarea v-if="type == 'textarea'" :disabled="disabled"></textarea>
    <input
      v-else
      :name="name"
      :type="type"
      :placeholder="placeholder"
      :value="value"
      :style="style"
      :required="required"
      :disabled="disabled"
    />
  </div>
</template>

<script>
export default {
  props: {
    type: {
      type: String,
      default: "text",
    },
    placeholder: {
      type: String,
      default: "",
    },
    value: {
      type: String,
      default: "",
    },
    style: {
      type: String,
      default: "",
    },
    name: {
      type: String,
      default: "",
    },
    required: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  setup(props) {
    const metodo = () => {
      console.warn('La propiedad "to" no está definida para la navegación.');
    };
    const capitalizeFirstLetter = (str) => {
      return str.charAt(0).toUpperCase() + str.slice(1);
    };

    return {
      metodo,
      capitalizeFirstLetter,
    };
  },
};
</script>
<style lang="css">
input {
  outline: none;
  border: none;
  padding: 10px;
  border-radius: 50px;
}
label {
  padding-left: 15px;
  text-align: left;
}

.container_input {
  width: 100%;
  display: flex;
  flex-direction: column;
}
</style>
