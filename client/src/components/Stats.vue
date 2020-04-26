<template>
  <div class="ma-12 text-center">
    <h2>{{user.name}} has finished learning! The summary of {{ isGirl2ndForm }} learning process is shown below.</h2>
    <p
      class="px-4 mt-6"
    >If taught by our model {{ isGirl }} would have ended in {{ stories.length }} steps. Because we forced listening {{ isGirl }} needed {{ stories.length + createdPath.length }}.</p>
    <img
      class="my-6 img"
      :src="require('../assets/' + user.name + '_with_forced_' + learningChartType + '.png')"
      alt
    />
    <img class="my-6 img" :src="require('../assets/' + user.name + '_ratio_of_actions.png')" />
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState({
      user: state => state.user,
      chosenPath: state => state.chosenPath,
      createdPath: state => state.createdPath,
      stories: state => state.stories
    }),
    learningChartType() {
      return this.chosenPath === "visual" ? "visuals" : this.chosenPath;
    },
    isGirl() {
      return this.user.name === "Yara" ? "she" : "he";
    },
    isGirl2ndForm() {
      return this.user.name === "Yara" ? "her" : "his";
    }
  }
};
</script>

<style lang="scss" scoped>
.img {
  width: 100%;
}
</style>