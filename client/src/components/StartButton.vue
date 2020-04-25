<template>
  <button @click="nextStep" class="button button-active">Start learning</button>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "StartButton",
  methods: {
    ...mapActions(["changeStep"]),
    nextStep() {
      this.changeStep(1);
    },
  },
};
</script>
