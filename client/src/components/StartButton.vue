<template>
  <button class="button button-active">Start learning</button>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "StartButton",
  methods: {
    ...mapActions({}),
  },
};
</script>
