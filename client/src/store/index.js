import Vue from "vue";
import Vuex from "vuex";
import storiesJSON from "../assets/jsonForDevelopment.json";

Vue.use(Vuex);

const emptyUser = {
  name: "",
  age: "",
  description: "",
};

export default new Vuex.Store({
  state: {
    currentStep: 1,
    steps: [
      { id: 0, description: "Start state" },
      { id: 1, description: "Highlight app description" },
    ],
    user: { ...emptyUser },
    stories: [],
  },
  mutations: {
    NEXT_STEP(state) {
      state.currentStep += 1;
    },
    GO_TO_FIRST_STEP(state) {
      state.currentStep = 1;
    },
    CHOOSE_USER(state, payload) {
      state.user = payload;
    },
    RESET_USER(state) {
      state.user = { ...emptyUser };
    },
    LOAD_STORIES(state, payload) {
      state.stories = payload;
    },
  },
  actions: {
    changeStep({ commit }, payload) {
      if (payload && payload !== 0) {
        commit("NEXT_STEP");
      } else {
        commit("GO_TO_FIRST_STEP");
        commit("RESET_USER");
      }
    },
    chooseUser({ commit, dispatch }, payload) {
      commit("CHOOSE_USER", payload);
      dispatch("loadStories");
    },
    loadStories({ commit }) {
      const stories = Object.keys(storiesJSON)
        .sort((a, b) => a - b)
        .map((story) => storiesJSON[story])
        .map((story) => {
          if (story.action === "train") {
            return {
              ...story,
              improvement: story.improvement.toFixed(3),
              skills: story.skills.map((skill) => skill.toFixed(3)),
            };
          }
          return {
            ...story,
            test_score: story.test_score.toFixed(3),
            skills: story.skills.map((skill) => skill.toFixed(3)),
          };
        });

      commit("LOAD_STORIES", stories);
    },
  },
  modules: {},
});
