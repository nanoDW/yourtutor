<template>
  <div class="start-learning-bg">
    <button @click="nextStep" v-if="currentStep === 3" class="button button-active">Start learning</button>
    <Homework :current-step="currentStep" />
    <Magazine :current-step="currentStep" />
    <Headset :current-step="currentStep" />
    <Webinar :current-step="currentStep" />
  </div>
</template>

<script>
import { mapActions } from "vuex";
import Homework from "../svg/Homework.vue";
import Magazine from "../svg/Magazine.vue";
import Headset from "../svg/Headset.vue";
import Webinar from "../svg/Webinar.vue";

export default {
  name: "StartButton",
  props: ["currentStep"],
  components: {
    Homework,
    Magazine,
    Headset,
    Webinar,
  },
  methods: {
    ...mapActions(["changeStep"]),
    nextStep() {
      this.changeStep(1);
    },
  },
};
</script>

<style src="../styles/start-button.scss" lang="scss" />
