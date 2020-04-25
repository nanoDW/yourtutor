<template>
  <div class="description" :class="{ active: isActive, 'box-shadow': !isActive }">
    <v-card flat tile height="100%">
      <p>
        We would like to give you a taste of how Artificial Intelligence can be used to provide students with tailored
        education materials. Everyone has their own way of learning and gains knowledge and skills at a different pace
        for each topic. Our solution can build thousands of models with goal to achieve highest learning efficiency with
        respect to student's potential in different areas and provide a personalised learning path.
      </p>
      <p>
        We present our solution on two actors - students - for which we built customised models for foreign language
        learning, to show their personalised learning paths prepared by our solution.
      </p>
      <v-row v-if="isActive">
        <v-col cols="9"></v-col>
        <button @click="nextStep" class="button button-active">Next</button>
      </v-row>
    </v-card>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  computed: {
    ...mapState({
      currentStep: (state) => state.currentStep,
    }),
    isActive() {
      return this.currentStep === 1;
    },
  },
  methods: {
    ...mapActions(["changeStep"]),
    nextStep() {
      this.changeStep(1);
    },
  },
};
</script>

<style src="../styles/description.scss" lang="scss"></style>
