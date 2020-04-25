<template>
  <v-row>
    <v-col cols="3">
      <v-row>
        <Logo @click.native="goToWelcomeScreen" />
      </v-row>
      <v-row class="px-6">
        <User :user="user" />
      </v-row>
    </v-col>
    <v-col cols="6">Center</v-col>
    <v-col cols="3">Right side</v-col>
  </v-row>
</template>

<script>
import { mapActions, mapState } from "vuex";
import Logo from "../shared/Logo";
import User from "../components/User";

export default {
  components: { Logo, User },
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
};
</script>
