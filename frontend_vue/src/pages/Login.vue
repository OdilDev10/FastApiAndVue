<template lang="">
   <section class="section_inicio">
    <div class="container">
        
    <div class="buttons_container">
        Login
    </div>

      <div class="container_inputs">
        <h1>LISTA APP</h1>
        <Input/>
      </div>

    </div>
   </section>
</template>

<script>
import Input from '../components/Input.vue'

export default {
    components: {
        Input
    },
    //   data() {
    //     return {
    //       notesPresentation: notesPresentation,
    //     };
    //   },
}
</script>


<style lang="">
.container_inputs {
  width: 70%;
}


.buttons_container {
  gap: 10px;
  display: flex;
  flex-direction: column;
  width: 20%;
}

</style>