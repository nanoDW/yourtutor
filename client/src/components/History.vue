<template>
  <div class="history" ref="history" :class="{ active: isActive }">
    <v-card
      height="100%"
      style="border-radius: 1.75rem !important; !important; overflow: scroll;"
      class="pa-4"
    >
      <div class="history-locked" v-if="currentStep < 4">
        <calendar />
        <p class="d">Press "Start learning" to show user's history</p>
        <count />
      </div>
      <v-expansion-panels v-else>
        <v-expansion-panel v-for="story in loadedStories" :key="story.step">
          <v-expansion-panel-header>
            <div class="history-element-header">
              {{ story.step }}.
              <span v-if="story.action === `train`">
                <b>Learning</b> -
                <Improvement />
                {{ story.improvement }}
              </span>
              <span v-else>
                <b>Testing</b> -
                <TestScore />
                {{ story.test_score }}
              </span>
            </div>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <p>
              <b>Subject</b>
              : {{ story.subject }}
            </p>
            <p>
              <b>Difficulty</b>
              : {{ story.difficulty }}
            </p>
            <p>
              <b>Skills</b>
              : {{ returnSkillsAsAString(story.skills) }}
            </p>
            <p v-if="story.action === 'train'">
              <b>Learning type</b>
              : {{ story.learning_type }}
            </p>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-card>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import Calendar from "../svg/Calendar.vue";
import Count from "../svg/Count.vue";
import Improvement from "../svg/Improvement.vue";
import TestScore from "../svg/TestScore.vue";

export default {
  components: { Calendar, Count, Improvement, TestScore },
  data() {
    return {
      loadedStories: []
    };
  },
  computed: {
    ...mapState({
      currentStep: state => state.currentStep,
      stories: state => state.stories,
      createdPath: state => state.createdPath
    }),
    isActive() {
      return this.currentStep === 4 || this.currentStep === 6;
    }
  },
  methods: {
    ...mapActions(["changeStep"]),
    returnSkillsAsAString(skills) {
      return skills.join(", ");
    },
    simulateLearning(stories) {
      let loadedStoriesAmount = 0;
      const interval = setInterval(() => {
        if (loadedStoriesAmount < stories.length) {
          this.loadedStories.unshift(stories[loadedStoriesAmount]);
          loadedStoriesAmount += 1;

          if (loadedStoriesAmount === stories.length) {
            this.changeStep(1);
            clearInterval(interval);
          }
        } else {
          this.changeStep(1);
        }
      }, 500);

      return 0;
    },
    simulateLoadingData() {
      this.simulateLearning(this.stories);
    },
    simulateTraining() {
      this.simulateLearning(this.createdPath);
    }
  },
  watch: {
    isActive() {
      if (this.isActive) {
        this.$refs.history.scrollIntoView();
        this.currentStep === 4
          ? this.simulateLoadingData()
          : this.simulateTraining();
      }
    }
  }
};
</script>

<style src="../styles/history.scss" lang="scss"></style>
