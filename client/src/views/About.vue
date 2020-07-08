<template>
  <v-row>
    <v-col cols="12" md="6" lg="3" class="logo-order">
      <v-row>
        <Logo @click.native="goToWelcomeScreen" />
      </v-row>
      <v-row class="px-6 mt-12">
        <v-card v-if="user.name" class="pt-8 mx-auto" style="border-radius: 1.75rem !important;">
          <User :user="user" />
        </v-card>
      </v-row>
    </v-col>
    <v-col cols="12" md="12" lg="6" class="my-12 container-order">
      <AppContainer />
    </v-col>
    <v-col cols="12" md="6" lg="3" class="my-12 history-order">
      <History />
    </v-col>
  </v-row>
</template>

<script>
import { mapActions, mapState } from "vuex";
import Logo from "../shared/Logo";
import User from "../components/User";
import AppContainer from "../components/Container";
import History from "../components/History.vue";

export default {
  components: { Logo, User, AppContainer, History },
  methods: {
    ...mapActions(["changeStep"]),
    goToWelcomeScreen() {
      this.changeStep();
      this.$router.push("/");
    },
  },
  mounted() {
    if(window) window.scrollTo(0, 0);
  },
  computed: {
    ...mapState({
      user: (state) => state.user,
    }),
  },
  created() {
    if (!this.user.name) {
      this.$router.push("/");
    }
  },
};
</script>

<style src="../styles/about.scss" lang="scss" scoped />