<template>
  <div class="history" :class="{ active: isActive }">
    <v-card
      style="border-radius: 1.75rem !important; height:calc(100vh - 24px) !important; max-height: 100vh; overflow: scroll"
      class="pa-4"
    >
      <p v-if="currentStep < 4">Press "Start learning" to show user's history</p>
      <div v-else v-for="story in loadedStories" :key="story.step" class="history-element">
        <p>{{ story.step }}. action: {{ story.action }}</p>
        <p>subject: {{ story.subject }}</p>
        <p>difficulty: {{ story.difficulty }}</p>
        <p>test score: {{ story.test_score }}</p>
        <p>reward: {{ story.reward }}</p>
        <div>skills: {{ returnSkillsAsAString(story.skills) }}</div>
        <p v-if="story.action === 'train'">improvement: {{ story.improvement }}</p>
        <p v-if="story.action === 'train'">learning type: {{ story.learning_type }}</p>
        <p v-if="story.action === 'train'">episode: {{ story.episode }}</p>
      </div>
    </v-card>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data() {
    return {
      loadedStories: [],
    };
  },
  computed: {
    ...mapState({
      currentStep: (state) => state.currentStep,
      stories: (state) => state.stories,
    }),
    isActive() {
      return this.currentStep === 4;
    },
  },
  methods: {
    ...mapActions(["changeStep"]),
    returnSkillsAsAString(skills) {
      return skills.join(", ");
    },
    simulateLoadingData() {
      let loadedStoriesAmount = 0;
      const interval = setInterval(() => {
        if (loadedStoriesAmount < this.stories.length) {
          this.loadedStories.unshift(this.stories[loadedStoriesAmount]);
          loadedStoriesAmount += 1;
        }
      }, 0);

      if (loadedStoriesAmount === this.stories.length) {
        clearInterval(interval);
        this.changeStep(1);
      }
      return 0;
    },
  },
  watch: {
    isActive() {
      if (this.isActive) {
        this.simulateLoadingData();
      }
    },
  },
};
</script>

<style src="../styles/history.scss" lang="scss"></style>
