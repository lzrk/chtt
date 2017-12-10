<template>
  <div id="app" class="container">
    <div class="row">
      <div class="col-sm">
        One of three columns
      </div>
      <div class="col-sm">
        <chtt-input></chtt-input>
      </div>
      <div class="col-sm">
        One of three columns
      </div>
    </div>  
  </div>
</template>

<script>
import ChttInput from './components/Input.vue'

export default {
  name: "app",
  components: {
    ChttInput
  },
  data() {
    return {
      msg: "Welcome to Your Vue.js App"
    };
  }
};
</script>

<style>

</style>
