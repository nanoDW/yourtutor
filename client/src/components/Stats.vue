<template>
  <div class="ma-12 text-center">
    <h2>{{user.name}} has finished learning! The summary of learning process is shown below.</h2>
    <p class="px-4 mt-6">{{ userStory }}</p>
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
    userStory() {
      if (this.user.name === "James") {
        if (this.chosenPath === "visual") {
          return `James with forced visuals: If taught by our model he would have ended in 267 steps. Because we forced visual learning he needed 355`;
        }
        return `James with forced reading: If taught by our model he would have ended in 267 steps. Because we forced reading he needed 380`;
      }

      if (this.chosenPath === "listening") {
        return `Yara with forced listening: If taught by our model she would have ended in 194 steps. Because we forced listening she needed 323`;
      }

      return `Yara with forced reading: If taught by our model she would have ended in 194 steps. Because we forced reading she needed 367`;
    }
  }
};
</script>

<style lang="scss" scoped>
.img {
  width: 100%;
}
</style>