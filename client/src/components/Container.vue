<template>
  <div ref="container" class="content-container" :class="{ active: isActive }">
    <v-card height="100%" style="border-radius: 1.75rem !important;  ">
      <div
        class="d-flex flex-wrap align-center justify-center"
        style="height: 100%; overflow: scroll"
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
import Stats from "./Stats.vue";

export default {
  components: {},
  computed: {
    ...mapState({
      user: state => state.user,
      currentStep: state => state.currentStep
    }),
    isActive() {
      return (
        this.currentStep === 3 ||
        this.currentStep === 5 ||
        this.currentStep === 7
      );
    },
    component() {
      switch (this.currentStep) {
        case 3:
          return StartButton;
        case 5:
          return LearningPath;
        case 7:
          return Stats;
        default:
          return StartButton;
      }
    }
  },
  watch: {
    isActive() {
      if (this.isActive) {
        this.$refs.container.scrollIntoView();
      }
    }
  }
};
</script>

<style src="../styles/container.scss" lang="scss"></style>
