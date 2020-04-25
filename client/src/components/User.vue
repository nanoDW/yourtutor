<template>
  <div class="user">
    <div class="img-background">
      <img class="img" :src="require('../assets/' + user.img + '')" />
    </div>
    <div class="bio">
      <v-row class="user-personal" align="center" justify="center">{{ userPersonalData }}</v-row>
      <v-row>
        <div class="bio-bg">
          {{ user.description }}
        </div>
      </v-row>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  props: ["user"],
  computed: {
    userPersonalData() {
      return `${this.user.name}, ${this.user.age} yo`;
    },
  },
  methods: {
    ...mapActions(["chooseUser", "changeStep"]),
  },
};
</script>
