<template>
  <div class="start-learning-bg">
    <button @click="nextStep" class="button button-active">Start learning</button>
  </div>
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

<style src="../styles/start-button.scss" lang="scss" />
