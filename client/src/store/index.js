import Vue from "vue";
import Vuex from "vuex";

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
    chooseUser({ commit }, payload) {
      commit("CHOOSE_USER", payload);
    },
  },
  modules: {},
});
