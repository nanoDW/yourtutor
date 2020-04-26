<template>
  <div class="ma-12 text-center">
    <h2>{{user.name}} has finished learning! Stats of the learning process are placed below.</h2>
    <img
      class="my-6 img"
      :src="require('../assets/' + user.name + '_' + learningChartType + '.png')"
      alt
    />
    <img class="my-6 img" :src="require('../assets/' + user.name + '_actions.png')" />
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState({
      user: state => state.user,
      chosenPath: state => state.chosenPath
    }),
    learningChartType() {
      return this.chosenPath === "visual" ? "visuals" : this.chosenPath;
    }
  }
};
</script>

<style lang="scss" scoped>
.img {
  width: 100%;
}
</style>