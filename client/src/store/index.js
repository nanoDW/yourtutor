import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const emptyUser = {
  name: "",
  age: "",
  description: "",
  type: "",
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
    createdPath: [],
    chosenPath: "",
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
    CREATE_PATH(state, payload) {
      state.createdPath = payload;
    },
    CHOOSE_PATH(state, payload) {
      state.chosenPath = payload;
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
    async loadStories({ state, commit }) {
      const storiesJSON = await import(`../assets/${state.user.name}_org.json`);
      const stories = Object.keys(storiesJSON.default).map((story) => storiesJSON[story]);

      commit("LOAD_STORIES", stories);
    },
    async chooseLearningType({ commit, state }, payload) {
      const short = payload === "visual" ? "vis" : payload.substring(0, 4);

      const storiesJSON = await import(`../assets/${state.user.name}_forced_${short}`);

      const stories = Object.keys(storiesJSON).map((story) => storiesJSON[story]);

      commit("CHOOSE_PATH", payload);
      commit("CREATE_PATH", stories);
    },
  },

  modules: {},
});
