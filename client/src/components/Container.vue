<template>
  <div class="content-container" :class="{ active: isActive }">
    <v-card height="100%" style="border-radius: 1.75rem !important;">
      <div
        class="d-flex flex-wrap align-center justify-center"
        style="height: 100%; overflow:hidden"
      >
        <component :is="component" :currentStep="currentStep" />
      </div>
    </v-card>
  </div>
</template>

<script>
import { mapState } from "vuex";
import StartButton from "./StartButton";
import LearningPath from "./LearningPath.vue";

export default {
  components: {},
  computed: {
    ...mapState({
      user: state => state.user,
      currentStep: state => state.currentStep
    }),
    isActive() {
      return this.currentStep === 3 || this.currentStep === 5;
    },
    component() {
      switch (this.currentStep) {
        case 3:
          return StartButton;
        case 5:
          return LearningPath;
        default:
          return StartButton;
      }
    }
  }
};
</script>

<style src="../styles/container.scss" lang="scss"></style>
