<template>
  <div class="content-container" :class="{ active: isActive }">
    <v-card style="border-radius: 1.75rem !important; height:100% !important" class="pa-12">
      <div class="d-flex flex-wrap align-center justify-center" style="height: 100%">
        <component :is="component" />
      </div>
    </v-card>
  </div>
</template>

<script>
import { mapState } from "vuex";
import StartButton from "./StartButton";

export default {
  components: { StartButton },
  computed: {
    ...mapState({
      user: (state) => state.user,
      currentStep: (state) => state.currentStep,
    }),
    isActive() {
      return this.currentStep === 3;
    },
    component() {
      switch (this.currentStep) {
        case 3:
          return StartButton;
        default:
          return StartButton;
      }
    },
  },
};
</script>

<style src="../styles/container.scss" lang="scss"></style>
