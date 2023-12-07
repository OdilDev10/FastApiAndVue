<template lang="">
    <input :type="type" :placeholder="placeholder" :value="value"/>
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
            default: '',
        },
        value: {
            type: String,
            default: '',
        },
    },
    setup(props) {

        const metodo = () => {
            console.warn('La propiedad "to" no está definida para la navegación.');
        };

        return {
            metodo,
        };
    },

}
</script>
<style lang="">
    
</style>