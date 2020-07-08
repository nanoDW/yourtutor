<template>
  <div ref="users" style="width: 100%">
    <v-row class="align-stretch">
      <v-col cols="12" md="6" class="d-flex flex-wrap align-end">
        <div class="users" :class="{ active: isActive, 'box-shadow': !isActive }">
          <v-card
            flat
            tile
            height="100%"
            style="display: flex; flex-wrap: wrap; justify-content: center; align-items: stretch"
          >
            <User :user="girl" :is-active="isActive" />
            <div class="text-center d-flex" style="flex-wrap:wrap; align-items: flex-end">
              <button
                class="button"
                @click="selectUser(girl)"
                :class="{ 'button-active': isActive }"
                :disabled="!isActive"
              >Choose {{ girl.name }}</button>
            </div>
          </v-card>
        </div>
      </v-col>

      <v-col cols="12" md="6" class="d-flex flex-wrap align-end">
        <div class="users" :class="{ active: isActive, 'box-shadow': !isActive }">
          <v-card
            flat
            tile
            height="100%"
            style="display: flex; flex-wrap: wrap; justify-content: center; align-items: stretch"
          >
            <User :user="boy" :is-active="isActive" />
            <div class="text-center d-flex" style="flex-wrap:wrap; align-items: flex-end">
              <button
                class="button"
                @click="selectUser(boy)"
                :class="{ 'button-active': isActive }"
                :disabled="!isActive"
              >Choose {{ boy.name }}</button>
            </div>
          </v-card>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import User from "./User";
export default {
  components: { User },
  computed: {
    ...mapState({
      currentStep: state => state.currentStep
    }),
    isActive() {
      return this.currentStep === 2;
    },
    girl() {
      return {
        img: "girl.png",
        name: "Yara",
        age: 9,
        description:
          "Yara likes to learn from illustrated books, her favourite one is a geographical atlas with maps and photos from different locations. She also enjoys watching morning shows with foreign language classes as she can easily link meanings of words with their visual shapes.",
        type: "visual"
      };
    },
    boy() {
      return {
        img: "boy.png",
        name: "James",
        age: 8,
        description:
          "James loves to join his grandma in listening to poetic radio broadcasts as it makes his imagination visit all the places and times from the readings. He quickly grasps new words by hearing multiple descriptions and various ways of their pronunciation.",
        type: "listening"
      };
    }
  },
  methods: {
    ...mapActions(["changeStep", "chooseUser"]),
    nextStep() {
      this.$router.push("/app");
      this.changeStep(1);
    },
    selectUser(user) {
      this.chooseUser(user);
      this.$router.push("/app");
      this.changeStep(1);
    }
  },
  watch: {
    isActive() {
      if (this.isActive) {
        this.$refs.users.scrollIntoView();
      }
    }
  }
};
</script>

<style src="../styles/users.scss" lang="scss"></style>
