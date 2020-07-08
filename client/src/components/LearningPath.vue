<template>
  <div class="mx-12 learning-path">
    <div>
      <h2
        class="text-center"
      >Our model identified {{ user.name }} is a {{ user.type }} type of learner. Please choose a different learning path to see how it impacts her learning performance.</h2>
      <div class="text-center mt-6">
        <button
          v-for="type in availableTypes"
          :key="type"
          @click="chooseType(type)"
          class="button button-active"
        >{{type}}</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: {
    ...mapState({
      user: state => state.user
    }),
    availableTypes() {
      return ["visual", "listening", "reading"].filter(
        el => el !== this.user.type
      );
    }
  },
  methods: {
    ...mapActions(["chooseLearningType", "changeStep"]),
    chooseType(type) {
      this.chooseLearningType(type).then(() => {
        this.changeStep(1);
      })
    }
  }
};
</script>

<style lang="scss" scoped>
.learning-path {
  background: url("../assets/opacity.png");
  height: 100%;
  width: 100%;
  background-size: 100% auto;

  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}
</style>