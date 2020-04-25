<template>
  <v-row>
    <v-col cols="3">
      <v-row>
        <Logo @click.native="goToWelcomeScreen" />
      </v-row>
      <v-row class="px-6 mt-12">
        <v-card v-if="user.name" class="pt-8" style="border-radius: 1.75rem !important;">
          <User :user="user" />
        </v-card>
      </v-row>
    </v-col>
    <v-col cols="6" class="my-12">
      <AppContainer />
    </v-col>
    <v-col cols="3">Right side</v-col>
  </v-row>
</template>

<script>
import { mapActions, mapState } from "vuex";
import Logo from "../shared/Logo";
import User from "../components/User";
import AppContainer from "../components/Container";

export default {
  components: { Logo, User, AppContainer },
  methods: {
    ...mapActions(["changeStep"]),
    goToWelcomeScreen() {
      this.changeStep();
      this.$router.push("/");
    },
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
