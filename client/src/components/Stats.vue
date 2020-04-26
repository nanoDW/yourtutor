<template>
  <div class="ma-12 text-center">
    <h2>{{user.name}} has finished learning! Stats of the learning process are placed below.</h2>
    <img class="my-6" src="../assets/Yara_listening.png" alt />
    <img class="my-6" src="../assets/James_actions.png" />
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState({
      user: state => state.user
    })
  }
};
</script>